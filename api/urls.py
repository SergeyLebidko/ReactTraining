from django.urls import path
from rest_framework import routers
from .views import random_msg, ProductViewSet, OrderViewSet, ClientViewSet, number_of_records, products_total_cost, \
    orders_total_cost, most_expensive_product, most_cheap_products, orders_cost_for_clients, labeled_orders, \
    clients_without_orders, client_video_and_cpu_orders, product_low

urlpatterns = [
    path('random_msg/', random_msg, name='random_msg'),
    path('number_of_records/', number_of_records, name='number_of_records'),
    path('products_total_cost/', products_total_cost, name='products_total_cost'),
    path('orders_total_cost/', orders_total_cost, name='orders_total_cost'),
    path('most_expensive_product/', most_expensive_product, name='most_expensive_product'),
    path('most_cheap_products/', most_cheap_products, name='most_cheap_products'),
    path('orders_cost_for_clients/', orders_cost_for_clients, name='orders_cost_for_clients'),
    path('labeled_orders/', labeled_orders, name='labeled_orders'),
    path('clients_without_orders/', clients_without_orders, name='clients_without_orders'),
    path('client_video_and_cpu_orders/', client_video_and_cpu_orders, name='client_video_and_cpu_orders'),
    path('product_low/', product_low, name='product_low')
]

router = routers.SimpleRouter()
router.register('products', ProductViewSet, basename='product')
router.register('orders', OrderViewSet, basename='order')
router.register('clients', ClientViewSet, basename='client')
urlpatterns.extend(router.urls)
