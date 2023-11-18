from rest_framework import routers
from django.urls import path, include
from .views import CategoryViewSet, ProductModelViewSet, CategoryListView, ProductListView, ProductDetailView

from .views import CategoryViewSet, ProductModelViewSet

products_router = routers.SimpleRouter()
products_router.register(r"products/category", CategoryViewSet)
products_router.register(r"products/product-model", ProductModelViewSet)

rlpatterns = [
    path('api/', include(routers.urls)),
    path('categories/', CategoryListView.as_view(), name='category_list'),
    path('categories/<int:pk>/products/', ProductListView.as_view(), name='product_list'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
]