from datetime import timezone

import factory
from django.contrib.auth import get_user_model
from factory.django import DjangoModelFactory

from ..models import Category, ProductModel

User = get_user_model()


class ProductModelFactory(DjangoModelFactory):
    class Meta:
        model = ProductModel

    updated_at = factory.Faker("date_time", tzinfo=timezone.utc)


class CategoryFactory(DjangoModelFactory):
    class Meta:
        model = Category

    category = factory.SubFactory("products.tests.factories.ProductModelFactory")
