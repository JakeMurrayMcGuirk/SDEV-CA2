# Generated by Django 4.2.7 on 2023-11-16 09:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("notification", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="notificationapp",
            name="user",
            field=models.ForeignKey(
                help_text="the user to whom this notification belongs",
                on_delete=django.db.models.deletion.CASCADE,
                related_name="notificationapps",
                to=settings.AUTH_USER_MODEL,
                verbose_name="user",
            ),
        ),
    ]
