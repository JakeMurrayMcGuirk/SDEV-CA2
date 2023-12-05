from rest_framework import routers

from .views import OderitemViewSet, OrderViewSet

orders_router = routers.SimpleRouter()
orders_router.register(r"orders/oderitem", OderitemViewSet)
orders_router.register(r"orders/order", OrderViewSet)

urlpatterns = [
    path('api/', include(orders_router.urls)), 
    path('checkout/', views.checkout_list, name='checkout'),
]
urlpatterns += orders_router.urls