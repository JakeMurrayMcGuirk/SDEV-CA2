from django.db import models


class ProductReview(models.Model):
    """
    Represents user reviews and ratings for products
    """

    product = models.ForeignKey(
        "products.ProductModel",
        related_name="product_reviews",
        on_delete=models.CASCADE,
        null=False,
        verbose_name="product ",
        help_text="the product for which the review is submitted ",
    )
    user = models.ForeignKey(
        "users.User",
        related_name="product_reviews",
        on_delete=models.CASCADE,
        null=False,
        verbose_name="user",
        help_text="the user which submitted the review ",
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
        help_text="the timestamo when the review was submitted",
    )

    def __str__(self):
        """String representation of a ProductReview instance."""
        return self.review_text
