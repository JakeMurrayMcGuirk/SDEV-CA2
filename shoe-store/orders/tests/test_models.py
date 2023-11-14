from django.test import TestCase

from ..models import Oderitem, Order
from .factories import OderitemFactory, OrderFactory


class OrderTestCase(TestCase):
    def test_create_order(self):
        """Test that Order can be created using its factory."""

        obj = OrderFactory()
        assert Order.objects.all().get() == obj


class OderitemTestCase(TestCase):
    def test_create_oderitem(self):
        """Test that Oderitem can be created using its factory."""

        obj = OderitemFactory()
        assert Oderitem.objects.all().get() == obj
