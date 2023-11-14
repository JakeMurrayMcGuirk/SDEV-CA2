from rest_framework import routers

from .views import BlogPostViewSet

blog_router = routers.SimpleRouter()
blog_router.register(r"blog/blog-post", BlogPostViewSet)
