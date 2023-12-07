from django.test import TestCase

from ..models import Cart, CartItem
from .factories import CartFactory, CartItemFactory


class CartTestCase(TestCase):
    def test_create_cart(self):
        """Test that Cart can be created using its factory."""

        obj = CartFactory()
        assert Cart.objects.all().get() == obj


class CartItemTestCase(TestCase):
    def test_create_cart_item(self):
        """Test that CartItem can be created using its factory."""

        obj = CartItemFactory()
        assert CartItem.objects.all().get() == obj
