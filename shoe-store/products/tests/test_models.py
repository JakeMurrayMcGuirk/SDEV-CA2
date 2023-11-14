from django.test import TestCase

from ..models import Category, ProductModel
from .factories import CategoryFactory, ProductModelFactory


class ProductModelTestCase(TestCase):
    def test_create_product_model(self):
        """Test that ProductModel can be created using its factory."""

        obj = ProductModelFactory()
        assert ProductModel.objects.all().get() == obj


class CategoryTestCase(TestCase):
    def test_create_category(self):
        """Test that Category can be created using its factory."""

        obj = CategoryFactory()
        assert Category.objects.all().get() == obj
