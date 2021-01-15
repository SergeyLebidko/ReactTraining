from django.urls import path
from rest_framework import routers
from .views import random_msg, ProductViewSet

urlpatterns = [
    path('random_msg/', random_msg, name='random_msg')
]

router = routers.SimpleRouter()
router.register('products', ProductViewSet, basename='product')
urlpatterns.extend(router.urls)
