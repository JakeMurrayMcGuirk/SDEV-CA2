from rest_framework import routers
from django.urls import path, include
from .views import WishlistitemViewSet
from . import views

wishlist_router = routers.SimpleRouter()
wishlist_router.register(r"wishlist/wishlistitem", WishlistitemViewSet)

app_name="wishlist"
urlpatterns = [
    path('add/<int:pk>', views.add_wishlist, name='add_wishlist'),
    path('', views.wishlist_detail, name='wishlist_detail'),
]