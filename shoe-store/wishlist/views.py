from rest_framework import viewsets

from . import permissions
from .models import Wishlistitem
from .serializers import WishlistitemSerializer


class WishlistitemViewSet(viewsets.ModelViewSet):
    queryset = Wishlistitem.objects.all()
    serializer_class = WishlistitemSerializer
    permission_classes = (permissions.WishlistitemPermission,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
