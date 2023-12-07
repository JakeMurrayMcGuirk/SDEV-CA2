from datetime import timezone

import factory
from django.contrib.auth import get_user_model
from factory.django import DjangoModelFactory

from ..models import Notificationapp

User = get_user_model()


class NotificationappFactory(DjangoModelFactory):
    class Meta:
        model = Notificationapp

    user = factory.SubFactory("users.tests.factories.UserFactory")
    messages = factory.Faker("text")
    notification_timestamp = factory.Faker("date_time", tzinfo=timezone.utc)
