from django.urls import path
from rest_framework import routers
from .views import random_msg, ProductViewSet, OrderViewSet, ClientViewSet, number_of_records, products_total_cost, \
    orders_total_cost, most_expensive_product, most_cheap_products, orders_cost_for_clients

urlpatterns = [
    path('random_msg/', random_msg, name='random_msg'),
    path('number_of_records/', number_of_records, name='number_of_records'),
    path('products_total_cost/', products_total_cost, name='products_total_cost'),
    path('orders_total_cost/', orders_total_cost, name='orders_total_cost'),
    path('most_expensive_product/', most_expensive_product, name='most_expensive_product'),
    path('most_cheap_products/', most_cheap_products, name='most_cheap_products'),
    path('orders_cost_for_clients/', orders_cost_for_clients, name='orders_cost_for_clients')
]

router = routers.SimpleRouter()
router.register('products', ProductViewSet, basename='product')
router.register('orders', OrderViewSet, basename='order')
router.register('clients', ClientViewSet, basename='client')
urlpatterns.extend(router.urls)
