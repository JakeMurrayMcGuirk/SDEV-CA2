# Generated by Django 4.2.5 on 2023-11-18 10:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("products", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="ProductReview",
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
                    "rating",
                    models.IntegerField(
                        default=1,
                        help_text="the numeric rating given by the user",
                        verbose_name="rating",
                    ),
                ),
                (
                    "review_text",
                    models.TextField(
                        default="",
                        help_text="The text content of the review",
                        verbose_name="review text",
                    ),
                ),
                (
                    "review_timestamp",
                    models.DateTimeField(
                        auto_now_add=True,
                        help_text="the timestamo when the review was submitted",
                        verbose_name="review timestamp",
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        help_text="the product for which the review is submitted ",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="product_reviews",
                        to="products.productmodel",
                        verbose_name="product ",
                    ),
                ),
            ],
        ),
    ]
