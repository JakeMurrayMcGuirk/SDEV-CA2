from datetime import timezone

import factory
from django.contrib.auth import get_user_model
from factory.django import DjangoModelFactory

from ..models import ProductReview

User = get_user_model()


class ProductReviewFactory(DjangoModelFactory):
    class Meta:
        model = ProductReview

    product = factory.SubFactory("products.tests.factories.ProductModelFactory")
    user = factory.SubFactory("users.tests.factories.UserFactory")
    review_timestamp = factory.Faker("date_time", tzinfo=timezone.utc)
