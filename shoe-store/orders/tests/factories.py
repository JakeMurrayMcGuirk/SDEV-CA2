from datetime import timezone

import factory
from django.contrib.auth import get_user_model
from factory.django import DjangoModelFactory

from ..models import Oderitem, Order

User = get_user_model()


class OrderFactory(DjangoModelFactory):
    class Meta:
        model = Order

    user = factory.SubFactory("users.tests.factories.UserFactory")
    updated_at = factory.Faker("date_time", tzinfo=timezone.utc)


class OderitemFactory(DjangoModelFactory):
    class Meta:
        model = Oderitem

    order = factory.SubFactory("orders.tests.factories.OrderFactory")
    product = factory.SubFactory("products.tests.factories.ProductModelFactory")
