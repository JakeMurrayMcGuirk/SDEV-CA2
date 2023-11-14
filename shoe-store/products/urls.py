from rest_framework import routers

from .views import CategoryViewSet, ProductModelViewSet

products_router = routers.SimpleRouter()
products_router.register(r"products/category", CategoryViewSet)
products_router.register(r"products/product-model", ProductModelViewSet)
