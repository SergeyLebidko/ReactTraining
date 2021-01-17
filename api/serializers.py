from rest_framework import serializers
from .models import Product, Order, Client


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):

    def to_representation(self, instance):
        result = serializers.ModelSerializer.to_representation(self, instance)
        result['client'] = instance.client.title
        result['product'] = instance.product.title
        return result

    class Meta:
        model = Order
        fields = '__all__'


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'
