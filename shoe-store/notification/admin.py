from django.contrib import admin

from .models import Notificationapp


class NotificationappAdmin(admin.ModelAdmin):
    model = Notificationapp
    search_fields = ["user", "messages", "is_read", "notification_timestamp"]
    list_select_related = True


admin.site.register(Notificationapp, NotificationappAdmin)
