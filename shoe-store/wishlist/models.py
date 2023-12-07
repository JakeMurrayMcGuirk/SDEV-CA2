from datetime import date

from django.db import models
from django.utils.timezone import now


class Wishlistitem(models.Model):
    """
    represents individual items within a users wishlist
    """

    user = models.ForeignKey(
        "users.User",
        related_name="wishlistitems",
        on_delete=models.CASCADE,
        null=False,
        verbose_name="user",
        help_text="user who owns this Wishlist",
    )
    product = models.ForeignKey(
        "products.ProductModel",
        related_name="wishlistitems",
        on_delete=models.CASCADE,
        null=False,
        verbose_name="product",
        help_text="the product added to the wishlist ",
    )
    added_timestamp = models.DateTimeField(
        null=False,
        default=now,
        verbose_name="added timestamp ",
        help_text="the timestamp when the product was added to the wishlist ",
    )
