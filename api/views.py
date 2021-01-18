import random
from django.db.models import F, Sum, Max, Min
from django.core.paginator import Paginator
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Product, Order, Client
from .serializers import ProductSerializer, OrderSerializer, ClientSerializer
from .pagination import CustomPagination


@api_view(['GET'])
def random_msg(request):
    msg_list = [
        'Привет!',
        'Пока!',
        'Как дела?',
        'Чем занимаешься?',
        'С новым годом и рождеством!',
        'Рад снова тебя видеть!',
        'Тебе понравилась новая книга?',
        'Пойдем на следующей неделе в кино?',
        'У меня все хорошо',
        'Я начал изучать React'
    ]
    return Response(
        {'answer': random.choice(msg_list)},
        headers={'Access-Control-Allow-Origin': '*'},
        status=status.HTTP_200_OK
    )


class ProductViewSet(ReadOnlyModelViewSet):
    serializer_class = ProductSerializer
    pagination_class = CustomPagination

    def get_queryset(self):
        queryset = Product.objects.order_by('title')
        search = self.request.query_params.get('search')
        if search:
            for param in search.split():
                queryset = queryset.filter(title__icontains=param)
        return queryset


class OrderViewSet(ReadOnlyModelViewSet):
    serializer_class = OrderSerializer
    pagination_class = CustomPagination
    queryset = Order.objects.all()


class ClientViewSet(ReadOnlyModelViewSet):
    serializer_class = ClientSerializer
    pagination_class = CustomPagination
    queryset = Client.objects.all()


@api_view(['GET'])
def number_of_records(request):
    products_count = Product.objects.count()
    orders_count = Order.objects.count()
    clients_count = Client.objects.count()
    resp = {
        'products_count': products_count,
        'orders_count': orders_count,
        'clients_count': clients_count
    }
    return Response(resp, status=status.HTTP_200_OK)


@api_view(['GET'])
def products_total_cost(request):
    """Суммарная стоимость всех товаров в БД"""
    total_cost_data = Product.objects.aggregate(total_cost=Sum(F('price') * F('balance')))
    return Response(total_cost_data, status=status.HTTP_200_OK)


@api_view(['GET'])
def orders_total_cost(request):
    """Суммарная стоимость всех заказов"""
    total_cost_data = Order.objects.aggregate(total_cost=Sum(F('count') * F('product__price')))
    return Response(total_cost_data, status=status.HTTP_200_OK)


@api_view(['GET'])
def most_expensive_product(request):
    """Список самых дорогих товаров"""
    products = Product.objects.filter(price=Product.objects.aggregate(max_price=Max(F('price')))['max_price'])
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def most_cheap_products(request):
    """Список самых дешевых товаров"""
    products = Product.objects.filter(price=Product.objects.aggregate(min_price=Min(F('price')))['min_price'])
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def orders_cost_for_clients(request):
    """Стоимость заказов каждого клиента"""
    clients = Client.objects.annotate(
        total_cost=Sum(F('order__count') * F('order__product__price'))
    ).filter(
        total_cost__isnull=False
    ).order_by(
        'title'
    )

    paginator = CustomPagination()
    page = paginator.paginate_queryset(clients, request)
    serializer = ClientSerializer(page, many=True, context={'additional_fields': ['total_cost']})

    return paginator.get_paginated_response(serializer.data)
