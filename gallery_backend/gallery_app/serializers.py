from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer, ReadOnlyField
from .models import Image


class ImageSerializer(ModelSerializer):
    class Meta:
        model = Image
        fields = "__all__"


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "email")


class CurrentUserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "email", "last_login")


class UserImagesSerializer(ModelSerializer):
    class Meta:
        model = Image
        fields = ("id", "image_url", "created_at")
