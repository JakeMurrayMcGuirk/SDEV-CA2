from django.test import TestCase

from ..models import ProductReview
from .factories import ProductReviewFactory


class ProductReviewTestCase(TestCase):
    def test_create_product_review(self):
        """Test that ProductReview can be created using its factory."""

        obj = ProductReviewFactory()
        assert ProductReview.objects.all().get() == obj
