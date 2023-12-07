from datetime import timezone

import factory
from django.contrib.auth import get_user_model
from factory.django import DjangoModelFactory

from ..models import Wishlistitem

User = get_user_model()


class WishlistitemFactory(DjangoModelFactory):
    class Meta:
        model = Wishlistitem

    user = factory.SubFactory("users.tests.factories.UserFactory")
    product = factory.SubFactory("products.tests.factories.ProductModelFactory")
