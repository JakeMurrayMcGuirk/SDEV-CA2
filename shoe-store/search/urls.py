from rest_framework import routers

from .views import ProductSearchViewSet

search_router = routers.SimpleRouter()
search_router.register(r"search/product-search", ProductSearchViewSet)
