from django.test import TestCase

from ..models import BlogPost
from .factories import BlogPostFactory


class BlogPostTestCase(TestCase):
    def test_create_blog_post(self):
        """Test that BlogPost can be created using its factory."""

        obj = BlogPostFactory()
        assert BlogPost.objects.all().get() == obj
