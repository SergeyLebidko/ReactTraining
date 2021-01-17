from django.urls import path
from rest_framework import routers
from .views import random_msg, ProductViewSet, OrderViewSet, ClientViewSet, number_of_records

urlpatterns = [
    path('random_msg/', random_msg, name='random_msg'),
    path('number_of_records/', number_of_records, name='number_of_records')
]

router = routers.SimpleRouter()
router.register('products', ProductViewSet, basename='product')
router.register('orders', OrderViewSet, basename='order')
router.register('clients', ClientViewSet, basename='client')
urlpatterns.extend(router.urls)
