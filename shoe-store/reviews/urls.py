from rest_framework import routers

from .views import ProductReviewViewSet

reviews_router = routers.SimpleRouter()
reviews_router.register(r"reviews/product-review", ProductReviewViewSet)

from django.urls import path
from .views import CreateReviewView
urlpatterns=[
    path('review/new/',CreateReviewView.as_view(),name='review_new'),
    #path('wishlist/new/',)
]