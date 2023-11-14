from rest_framework import viewsets

from . import permissions
from .models import Oderitem, Order
from .serializers import OderitemSerializer, OrderSerializer


class OderitemViewSet(viewsets.ModelViewSet):
    queryset = Oderitem.objects.all()
    serializer_class = OderitemSerializer
    permission_classes = (permissions.OderitemPermission,)


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = (permissions.OrderPermission,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
