from rest_framework import serializers

from .models import Notificationapp


class NotificationappSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notificationapp
        fields = ["id", "user", "messages", "is_read", "notification_timestamp"]
