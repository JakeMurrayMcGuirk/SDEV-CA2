from django.test import TestCase

from ..models import Notificationapp
from .factories import NotificationappFactory


class NotificationappTestCase(TestCase):
    def test_create_notificationapp(self):
        """Test that Notificationapp can be created using its factory."""

        obj = NotificationappFactory()
        assert Notificationapp.objects.all().get() == obj
