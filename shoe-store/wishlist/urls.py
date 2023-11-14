from rest_framework import routers

from .views import WishlistitemViewSet

wishlist_router = routers.SimpleRouter()
wishlist_router.register(r"wishlist/wishlistitem", WishlistitemViewSet)
