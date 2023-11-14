from datetime import date

from django.db import models
from django.utils.timezone import now


class ProductSearch(models.Model):
    """
    Represents the search functionality for product handling
    """

    product = models.ForeignKey(
        "products.ProductModel",
        related_name="product_searchs",
        on_delete=models.CASCADE,
        null=False,
        verbose_name="product ",
        help_text="The producr associatd with the search data",
    )
    search_query = models.CharField(
        max_length=255,
        null=False,
        verbose_name="search query",
        help_text="the search query enterd by the user ",
    )
    search_filters = models.JSONField(
        null=True,
        verbose_name="search filters ",
        help_text="Aditional filters applied to the search query ",
    )
    search_timestamp = models.DateTimeField(
        null=False,
        default=now,
        verbose_name="search timestamp ",
        help_text="The timestamp which the search was performed ",
    )

    def __str__(self):
        """String representation of a ProductSearch instance."""
        return self.search_query
