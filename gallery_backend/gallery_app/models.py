from django.db import models
from django.contrib.auth.models import User


class Image(models.Model):
    id = models.AutoField(primary_key=True)
    image_url = models.URLField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField()
