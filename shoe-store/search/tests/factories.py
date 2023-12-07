from datetime import timezone

import factory
from django.contrib.auth import get_user_model
from factory.django import DjangoModelFactory

from ..models import ProductSearch

User = get_user_model()


class ProductSearchFactory(DjangoModelFactory):
    class Meta:
        model = ProductSearch

    product = factory.SubFactory("products.tests.factories.ProductModelFactory")
    search_query = factory.Faker("bs")
