# Generated by Django 4.2.5 on 2023-11-18 10:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("reviews", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="productreview",
            name="user",
            field=models.ForeignKey(
                help_text="the user which submitted the review ",
                on_delete=django.db.models.deletion.CASCADE,
                related_name="product_reviews",
                to=settings.AUTH_USER_MODEL,
                verbose_name="user",
            ),
        ),
    ]
