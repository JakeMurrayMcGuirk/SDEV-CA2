from datetime import timezone

import factory
from django.contrib.auth import get_user_model
from factory.django import DjangoModelFactory

from ..models import Cart, CartItem

User = get_user_model()


class CartFactory(DjangoModelFactory):
    class Meta:
        model = Cart

    user = factory.SubFactory("users.tests.factories.UserFactory")
    updated_at = factory.Faker("date_time", tzinfo=timezone.utc)


class CartItemFactory(DjangoModelFactory):
    class Meta:
        model = CartItem

    cart = factory.SubFactory("cart.tests.factories.CartFactory")
    product = factory.SubFactory("products.tests.factories.ProductModelFactory")
