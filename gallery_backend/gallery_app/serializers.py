from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Image


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username")


class CurrentUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "email", "last_login")


class UserImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ("id", "image_url", "created_at")


class UserSingleImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ("id", "image_url", "created_at")
