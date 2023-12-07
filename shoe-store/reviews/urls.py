from rest_framework import routers

from .views import ProductReviewViewSet

reviews_router = routers.SimpleRouter()
reviews_router.register(r"reviews/product-review", ProductReviewViewSet)
