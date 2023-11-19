from rest_framework import routers
from django.urls import path, include
from .views import CategoryViewSet, ProductModelViewSet, CategoryListView, ProductListView, ProductDetailView, AllProductListView

products_router = routers.SimpleRouter()
products_router.register(r"products/category", CategoryViewSet)
products_router.register(r"products/product-model", ProductModelViewSet)

urlpatterns = [
    path('api/', include(products_router.urls)),
    path('products/all/', AllProductListView.as_view(), name='product_list'),
    path('categories/', CategoryListView.as_view(), name='category_list'),
    path('categories/<int:pk>/products/', ProductListView.as_view(), name='product_list'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
]

urlpatterns += products_router.urls
