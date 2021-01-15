import json
from django.core.management.base import BaseCommand
from api.models import Product


class Command(BaseCommand):

    def handle(self, *args, **options):
        Product.objects.all().delete()

        with open('product_data.txt') as file:
            for element in json.loads(file.read()):
                Product.objects.create(title=element['title'], price=element['price'])

        count = Product.objects.count()
        print(f'Импорт списка товаров выполнен. Импортировано {count} едениц')
