from django.contrib import admin
from .models import Product, Order, Client


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'balance']
    list_display_links = ['title']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['client', 'product', 'count']
    list_display_links = ['client', 'product', 'count']


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['title']
    list_display_links = ['title']
