import random
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
