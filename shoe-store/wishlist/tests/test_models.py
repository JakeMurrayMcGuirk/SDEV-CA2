from django.test import TestCase

from ..models import Wishlistitem
from .factories import WishlistitemFactory


class WishlistitemTestCase(TestCase):
    def test_create_wishlistitem(self):
        """Test that Wishlistitem can be created using its factory."""

        obj = WishlistitemFactory()
        assert Wishlistitem.objects.all().get() == obj
