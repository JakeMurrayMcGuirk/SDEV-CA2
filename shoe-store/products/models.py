from datetime import date
from decimal import Decimal
from django.db import models
from django.contrib.auth.models import User

class ProductModel(models.Model):
    category = models.ForeignKey(
        'Category', related_name="products", on_delete=models.CASCADE, null=True
    )
    name = models.CharField(
        max_length=255,
        null=False,
        default="none",
        verbose_name="Product Name",
        help_text="The name of the shoe product"
    )
    description = models.TextField(
        null=True,
        verbose_name="Product Description",
        help_text="A detailed description of the shoe product"
    )
    price = models.DecimalField(
        null=False,
        max_digits=50,
        decimal_places=2,
        default=Decimal("0.0"),
        verbose_name="Product Price",
        help_text="The price of the shoe product"
    )
    stock = models.IntegerField(
        null=False,
        default=0,
        verbose_name="Product Stock",
        help_text="The available quantity of the shoe product"
    )
    images = models.ImageField(
        upload_to="productmodel/images/",
        max_length=255,
        null=True,
        verbose_name="Product Image",
        help_text="An image representing the shoe product"
    )
    created_at = models.DateField(
        null=False,
        default=date.today,
        verbose_name="Created at",
        help_text="The timestamp indicating when the shoe product was created"
    )
    updated_at = models.DateTimeField(
        null=False,
        verbose_name="Updated at",
        help_text="The timestamp indicating when the shoe product was last updated"
    )

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=255, default='Default Category Name')

    def __str__(self):
        return self.name




class ProductReview(models.Model):
    product = models.ForeignKey(
        "products.ProductModel",
        related_name="product_reviews",
        on_delete=models.CASCADE,
        null=False,
        verbose_name="product",
        help_text="the product for which the review is submitted",
    )
    user = models.ForeignKey(
        User,
        related_name="product_reviews",
        on_delete=models.CASCADE,
        null=False,
        verbose_name="user",
        help_text="the user who submitted the review",
    )
    rating = models.IntegerField(
        null=False,
        default=1,
        verbose_name="rating",
        help_text="the numeric rating given by the user",
    )
    review_text = models.TextField(
        null=False,
        default="",
        verbose_name="review text",
        help_text="The text content of the review",
    )
    review_timestamp = models.DateTimeField(
        null=False,
        auto_now_add=True,
        verbose_name="review timestamp",
        help_text="the timestamp when the review was submitted",
    )

    def __str__(self):
        """String representation of a ProductReview instance."""
        return self.review_text