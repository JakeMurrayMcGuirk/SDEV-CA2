from datetime import date

from django.db import models
from django.utils.timezone import now


class Cart(models.Model):
    """
    represents the shopping cart for each user
    """

    user = models.OneToOneField(
        "users.User",
        related_name="cart",
        on_delete=models.CASCADE,
        null=False,
        unique=True,
        verbose_name="user",
        help_text="The user to whom this shopping cart belongs ",
    )
    created_at = models.DateTimeField(
        null=False,
        default=now,
        verbose_name="created at ",
        help_text="the timestamp indicating when the shopping cart was created ",
    )
    updated_at = models.DateTimeField(
        null=False,
        verbose_name="updated at ",
        help_text="the time stamp indicating when the shopping cart was last updated ",
    )


class CartItem(models.Model):
    """
    Represents individual items within the shopping cart
    """

    cart = models.ForeignKey(
        "cart.Cart",
        related_name="cart_items",
        on_delete=models.CASCADE,
        null=False,
        verbose_name="shopping cart ",
        help_text="The shopping cart to which this item belongs ",
    )
    product = models.ForeignKey(
        "products.ProductModel",
        related_name="cart_items",
        on_delete=models.CASCADE,
        null=False,
        verbose_name="product ",
        help_text="The prosuct included in this cart item ",
    )
    quantity = models.IntegerField(
        null=False,
        default=1,
        verbose_name="quantity ",
        help_text="the quantity of the products in this cart item ",
    )
