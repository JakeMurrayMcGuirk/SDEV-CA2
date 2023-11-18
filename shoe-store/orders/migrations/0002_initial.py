# Generated by Django 4.2.5 on 2023-11-18 10:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("orders", "0001_initial"),
        ("products", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="user",
            field=models.ForeignKey(
                help_text="The customer who places the order",
                on_delete=django.db.models.deletion.CASCADE,
                related_name="orders",
                to=settings.AUTH_USER_MODEL,
                verbose_name="customer",
            ),
        ),
        migrations.AddField(
            model_name="oderitem",
            name="order",
            field=models.ForeignKey(
                help_text="The order to which this item belongs",
                on_delete=django.db.models.deletion.PROTECT,
                related_name="oderitems",
                to="orders.order",
                verbose_name="order",
            ),
        ),
        migrations.AddField(
            model_name="oderitem",
            name="product",
            field=models.ForeignKey(
                help_text="The product included in this order item ",
                on_delete=django.db.models.deletion.CASCADE,
                related_name="oderitems",
                to="products.productmodel",
                verbose_name="Product",
            ),
        ),
    ]
