from rest_framework import routers
from django.urls import path, include
from .views import CategoryViewSet, ProductModelViewSet, CategoryListView, ProductListView, ProductDetailView, AllProductListView
from cart.views import add_to_cart 
from . import views

products_router = routers.SimpleRouter()
products_router.register(r"products/category", CategoryViewSet)
products_router.register(r"products/product-model", ProductModelViewSet)
APPNAME = 'products';

urlpatterns = [
    path('api/', include(products_router.urls)),
    path('products/all/', AllProductListView.as_view(), name='product_list'),
    path('categories/', CategoryListView.as_view(), name='category_list'),
    path('categories/<int:pk>/products/', ProductListView.as_view(), name='product_list'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('api/v1/products/add-to-cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('submit_review/', views.submit_review, name='submit_review'),
]
