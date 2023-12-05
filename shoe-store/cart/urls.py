from rest_framework import routers
from .views import CartItemViewSet, CartViewSet
from django.urls import path, include
from . import views
from django.urls import path 

cart_router = routers.SimpleRouter()
cart_router.register(r"cart/cart", CartViewSet)
cart_router.register(r"cart/cart-item", CartItemViewSet)

urlpatterns = [
    path('api/', include(cart_router.urls)), 
    path('cart/', views.cart, name='cart_list'),
    path('cart/detail', views.cart_detail, name='cart_detail'),
    path('cart/<uuid:product_id/', views.cart_remove, name='cart_remove'),

]
urlpatterns += cart_router.urls