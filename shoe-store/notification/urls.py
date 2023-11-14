from rest_framework import routers

from .views import NotificationappViewSet

notification_router = routers.SimpleRouter()
notification_router.register(r"notification/notificationapp", NotificationappViewSet)
