# Generated by Django 4.1.1 on 2022-09-15 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("gallery_app", "0003_alter_image_user_delete_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="image",
            name="created_at",
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
