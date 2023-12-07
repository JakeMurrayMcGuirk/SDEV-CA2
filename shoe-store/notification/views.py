from rest_framework import viewsets

from . import permissions
from .models import Notificationapp
from .serializers import NotificationappSerializer


class NotificationappViewSet(viewsets.ModelViewSet):
    queryset = Notificationapp.objects.all()
    serializer_class = NotificationappSerializer
    permission_classes = (permissions.NotificationappPermission,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
