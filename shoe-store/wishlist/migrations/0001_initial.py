# Generated by Django 4.2.5 on 2023-11-14 19:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("products", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Wishlistitem",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "added_timestamp",
                    models.DateTimeField(
                        default=django.utils.timezone.now,
                        help_text="the timestamp when the product was added to the wishlist ",
                        verbose_name="added timestamp ",
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        help_text="the product added to the wishlist ",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="wishlistitems",
                        to="products.productmodel",
                        verbose_name="product",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        help_text="user who owns this Wishlist",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="wishlistitems",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="user",
                    ),
                ),
            ],
        ),
    ]
