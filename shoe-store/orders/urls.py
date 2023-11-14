from rest_framework import routers

from .views import OderitemViewSet, OrderViewSet

orders_router = routers.SimpleRouter()
orders_router.register(r"orders/oderitem", OderitemViewSet)
orders_router.register(r"orders/order", OrderViewSet)
