from django.db import models


class Notificationapp(models.Model):
    """
    represents notifications for users, alerting them about relevant , events or updates
    """

    user = models.ForeignKey(
        "users.User",
        related_name="notificationapps",
        on_delete=models.CASCADE,
        null=False,
        verbose_name="user",
        help_text="the user to whom this notification belongs",
    )
    messages = models.TextField(
        null=False,
        verbose_name="message",
        help_text="The content of the notification message",
    )
    is_read = models.BooleanField(
        null=False,
        default=False,
        verbose_name="is read",
        help_text="indicates whether the user has read the notification ",
    )
    notification_timestamp = models.DateTimeField(
        null=False,
        auto_now_add=True,
        verbose_name="notification timestamp ",
        help_text="The timestamp whhen the notifaction was created",
    )

    def __str__(self):
        """String representation of a Notificationapp instance."""
        return self.messages
