import random
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Product
from .serializers import ProductSerializer
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
