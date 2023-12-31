# Generated by Django 4.2.5 on 2023-11-22 17:08

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0004_alter_blogpost_pub_date_alter_blogpost_title"),
    ]

    operations = [
        migrations.AddField(
            model_name="blogpost",
            name="image",
            field=models.ImageField(
                blank=True,
                help_text="Image related to the blog post",
                null=True,
                upload_to="blogmodel/images",
                verbose_name="Image",
            ),
        ),
    ]
