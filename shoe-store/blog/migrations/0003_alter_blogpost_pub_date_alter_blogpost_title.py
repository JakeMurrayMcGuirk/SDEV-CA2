# Generated by Django 4.2.5 on 2023-11-22 16:17

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0002_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blogpost",
            name="pub_date",
            field=models.DateTimeField(
                help_text="the date when the blog post ",
                null=True,
                verbose_name="publication date ",
            ),
        ),
        migrations.AlterField(
            model_name="blogpost",
            name="title",
            field=models.CharField(
                help_text="The title of the blog post ",
                max_length=255,
                verbose_name="title",
            ),
        ),
    ]
