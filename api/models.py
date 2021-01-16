from django.db import models
from .utils import random_val


class Product(models.Model):
    title = models.CharField(max_length=1000, verbose_name='Наименование')
    price = models.IntegerField(verbose_name='Цена')
    balance = models.IntegerField(verbose_name='Остаток на складе', default=random_val)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['title']


class Client(models.Model):
    title = models.CharField(max_length=100, verbose_name='Наименование')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'
        ordering = ['title']


class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name='Клиент')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Товар')
    count = models.IntegerField(verbose_name='Количество')

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
