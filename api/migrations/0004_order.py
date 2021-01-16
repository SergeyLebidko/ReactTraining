# Generated by Django 3.1.4 on 2021-01-16 10:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20210116_1258'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(verbose_name='Количество')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.client', verbose_name='Клиент')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.product', verbose_name='Товар')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
            },
        ),
    ]
