from rest_framework import routers
from django.urls import path, include

from .views import ProductReviewViewSet, ReviewCreateView

reviews_router = routers.SimpleRouter()
reviews_router.register(r"reviews/product-review", ProductReviewViewSet)
urlpatterns=[
    path('api/', include(reviews_router.urls)),
    path('review/new/', ReviewCreateView.as_view(),name='create_review')
]