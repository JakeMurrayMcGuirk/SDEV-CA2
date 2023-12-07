from datetime import timezone

import factory
from django.contrib.auth import get_user_model
from factory.django import DjangoModelFactory

from ..models import BlogPost

User = get_user_model()


class BlogPostFactory(DjangoModelFactory):
    class Meta:
        model = BlogPost

    author = factory.SubFactory("users.tests.factories.UserFactory")
    title = factory.Faker("bs")
    content = factory.Faker("text")
    pub_date = factory.Faker("date_time", tzinfo=timezone.utc)
