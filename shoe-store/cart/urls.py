from rest_framework import routers
from .views import CartItemViewSet, CartViewSet
from django.urls import path 

cart_router = routers.SimpleRouter()
cart_router.register(r"cart/cart", CartViewSet)
cart_router.register(r"cart/cart-item", CartItemViewSet)

