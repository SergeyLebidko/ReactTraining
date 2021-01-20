from rest_framework import serializers
from .models import Product, Order, Client


class ContextableSerializer(serializers.ModelSerializer):

    def to_representation(self, instance):
        result = serializers.ModelSerializer.to_representation(self, instance)
        additional_fields = self.context.get('additional_fields')
        if additional_fields:
            for field in additional_fields:
                result[field] = getattr(instance, field)
        return result


class ProductSerializer(ContextableSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class OrderSerializer(ContextableSerializer):

    def to_representation(self, instance):
        result = ContextableSerializer.to_representation(self, instance)
        result['client'] = instance.client.title
        result['product'] = instance.product.title
        return result

    class Meta:
        model = Order
        fields = '__all__'


class ClientSerializer(ContextableSerializer):
    class Meta:
        model = Client
        fields = '__all__'
