from django.test import TestCase

from ..models import ProductSearch
from .factories import ProductSearchFactory


class ProductSearchTestCase(TestCase):
    def test_create_product_search(self):
        """Test that ProductSearch can be created using its factory."""

        obj = ProductSearchFactory()
        assert ProductSearch.objects.all().get() == obj
