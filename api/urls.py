from django.urls import path
from rest_framework import routers
from .views import random_msg, ProductViewSet, OrderViewSet, ClientViewSet

urlpatterns = [
    path('random_msg/', random_msg, name='random_msg')
]

router = routers.SimpleRouter()
router.register('products', ProductViewSet, basename='product')
router.register('orders', OrderViewSet, basename='order')
router.register('clients', ClientViewSet, basename='client')
urlpatterns.extend(router.urls)
