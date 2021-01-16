import json
import random
from datetime import datetime
from django.core.management.base import BaseCommand
from api.models import Product, Order, Client


class Command(BaseCommand):

    def handle(self, *args, **options):
        Product.objects.all().delete()
        Client.objects.all().delete()

        # Первая временная метка
        t1 = datetime.now()

        # Загружаем товары
        products = []
        with open('product_data.txt') as file:
            for element in json.loads(file.read()):
                products.append(Product(title=element['title'], price=element['price']))
        Product.objects.bulk_create(products)
        products = Product.objects.all()
        product_count = len(products)

        # Загружаем клиентов
        clients = []
        with open('client_data.txt', encoding='utf-8') as file:
            for line in file:
                title = line[:-1]
                clients.append(Client(title=title))
        Client.objects.bulk_create(clients)
        clients = Client.objects.all()
        client_count = len(clients)

        # Создаем заказы
        order_count = 2000
        orders = []
        for _ in range(order_count):
            client = random.choice(clients)
            product = random.choice(products)
            count = random.randint(1, 100)
            orders.append(Order(client=client, product=product, count=count))
        Order.objects.bulk_create(orders)

        # Вторая временная метка
        t2 = datetime.now()
        execution_time = t2 - t1

        print(
            f'Создано: {product_count} товаров, '
            f'{client_count} клиентов, '
            f'{order_count} заказов. '
            f'Время выполнения: {execution_time}'
        )
