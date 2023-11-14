from datetime import date
from decimal import Decimal

from django.db import models


class ProductModel(models.Model):
    """
    Represents individual shoe products with attributes like name, description, price, stock, image, category, created_at, updated_at.
    """

    name = models.CharField(
        max_length=255,
        null=False,
        default="none",
        verbose_name="Product Name",
        help_text="The name of the shoe produc",
    )
    description = models.TextField(
        null=True,
        verbose_name="Product Discription",
        help_text="a detailed discription of the shoe product ",
    )
    price = models.DecimalField(
        null=False,
        max_digits=50,
        decimal_places=2,
        default=Decimal("0.0"),
        verbose_name="Product Price ",
        help_text="The price of the shoe product ",
    )
    stock = models.IntegerField(
        null=False,
        default=0,
        verbose_name="product stock ",
        help_text="The available quantity of the shoe product",
    )
    images = models.ImageField(
        upload_to="productmodel/images/",
        max_length=255,
        null=True,
        verbose_name="Product Image ",
        help_text="An image representing the shoe product ",
    )
    created_at = models.DateField(
        null=False,
        default=date.today,
        verbose_name="created at ",
        help_text="the timestamp indicating when the shoe product was created ",
    )
    updated_at = models.DateTimeField(
        null=False,
        verbose_name="updated at ",
        help_text="The timestap indicating when the shoe product was last updated ",
    )

    def __str__(self):
        """String representation of a ProductModel instance."""
        return self.name


class Category(models.Model):
    """
    category
    """

    category = models.ForeignKey(
        "products.ProductModel",
        related_name="categories",
        on_delete=models.CASCADE,
        null=False,
        verbose_name="category ",
        help_text="the ategory to which this produc belongs",
    )
