from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=1000, verbose_name='Наименование')
    price = models.IntegerField(verbose_name='Цена')

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
