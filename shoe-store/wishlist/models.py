from datetime import date

from django.db import models
from django.utils.timezone import now
from products.models import ProductModel

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

    class Meta:
        db_table = 'WishlistItem'
    
    def __str__(self):
        return self.product

class Wishlist(models.Model):
    wishlist_id = models.CharField(max_length=250, blank=True)
    date_added = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'Wishlist'
        ordering = ['date_added']
    
    def __str__(self):
        return self.cart_id