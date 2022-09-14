# Generated by Django 4.1.1 on 2022-09-13 15:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("gallery_app", "0002_rename_user_id_image_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="image",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.DeleteModel(
            name="User",
        ),
    ]