# Generated by Django 5.1.5 on 2025-02-14 20:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pizza_app', '0005_order_delivery_datetime'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='delivery_datetime',
        ),
    ]
