
from django.contrib import admin
from django.urls import include, path
from notification.urls import notification_router
from products.urls import products_router
from rest_framework import routers
from search.urls import search_router
from wishlist.urls import wishlist_router

from blog.urls import blog_router
from users.urls import users_router
from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()
router.registry.extend(blog_router.registry)
router.registry.extend(notification_router.registry)

router.registry.extend(products_router.registry)
router.registry.extend(search_router.registry)
router.registry.extend(wishlist_router.registry)
router.registry.extend(users_router.registry)

urlpatterns = [
    path('', include('users.urls')),
    path('api/v1/products/', include('products.urls')), 
    path('api/v1/blog/', include('blog.urls')), 
    path("admin/doc/", include("django.contrib.admindocs.urls")),
    path("admin/", admin.site.urls),
    path("api/docs/auth/", include("rest_framework.urls", namespace="rest_framework")),
    path("api/v1/auth/", include("dj_rest_auth.urls")),
    path("api/v1/auth/register/", include("dj_rest_auth.registration.urls")),
    path("api/v1/", include("openapi.urls")),
    path("api/v1/", include(router.urls)),
    path("cart/", include("cart.urls", namespace="cart")),
    path('api/v1/products/cart/', include('cart.urls')),
]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
  


# path('api/v1/orders/', include('orders.urls')),  
# path('api/v1/notifications/', include('notification.urls')),  
