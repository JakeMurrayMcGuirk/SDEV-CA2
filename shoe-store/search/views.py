from rest_framework import viewsets

from . import permissions
from .models import ProductSearch
from .serializers import ProductSearchSerializer


class ProductSearchViewSet(viewsets.ModelViewSet):
    queryset = ProductSearch.objects.all()
    serializer_class = ProductSearchSerializer
    permission_classes = (permissions.ProductSearchPermission,)
