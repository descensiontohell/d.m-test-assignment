from django.contrib.auth.models import User
from django.db import models


class Image(models.Model):
    id = models.AutoField(primary_key=True)
    image_url = models.URLField()
    user = models.ForeignKey(User, related_name="images", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
