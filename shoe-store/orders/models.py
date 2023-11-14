from datetime import date
from decimal import Decimal

from django.db import models
from django.utils.timezone import now


class Order(models.Model):
    """
    Represents customer orders wuth attributes like user (ForeignKey to the custum use model)
    """

    user = models.ForeignKey(
        "users.User",
        related_name="orders",
        on_delete=models.CASCADE,
        null=False,
        verbose_name="customer",
        help_text="The customer who places the order",
    )
    created_at = models.DateTimeField(
        null=False,
        default=now,
        verbose_name="created at ",
        help_text="The timestamp indicating when the order was created ",
    )
    updated_at = models.DateTimeField(
        null=False,
        verbose_name="updated at ",
        help_text="the timestamp indicating when the order was last updated ",
    )
    total_amount = models.DecimalField(
        null=False,
        max_digits=100000,
        decimal_places=2,
        default=Decimal("0.00"),
        verbose_name="total amount ",
        help_text="the total amount for the order ",
    )


class Oderitem(models.Model):
    """
    represents individual items within an order
    """

    order = models.ForeignKey(
        "orders.Order",
        related_name="oderitems",
        on_delete=models.PROTECT,
        null=False,
        verbose_name="order",
        help_text="The order to which this item belongs",
    )
    product = models.ForeignKey(
        "products.ProductModel",
        related_name="oderitems",
        on_delete=models.CASCADE,
        null=False,
        verbose_name="Product",
        help_text="The product included in this order item ",
    )
    quantity = models.IntegerField(
        null=False,
        default=1,
        verbose_name="quantity",
        help_text="the quantity of the product in this order item ",
    )
    price = models.DecimalField(
        null=False,
        max_digits=1000000,
        decimal_places=2,
        default=Decimal("0.0"),
        verbose_name="price ",
        help_text="the price of a single unit of the product in this orde ritem ",
    )
