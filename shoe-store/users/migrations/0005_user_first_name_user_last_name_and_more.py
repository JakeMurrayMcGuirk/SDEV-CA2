# Generated by Django 4.2.5 on 2023-11-19 14:57

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0004_remove_user_first_name_remove_user_last_name"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="first_name",
            field=models.CharField(
                default="",
                help_text="User's first name",
                max_length=30,
                verbose_name="First Name",
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="last_name",
            field=models.CharField(
                default="",
                help_text="User's last name",
                max_length=150,
                verbose_name="Last Name",
            ),
        ),
        migrations.AlterField(
            model_name="userprofile",
            name="profile_picture",
            field=models.ImageField(blank=True, null=True, upload_to="profile/"),
        ),
    ]
