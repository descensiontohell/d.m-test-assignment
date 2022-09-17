from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer
from .models import Image


class AdminImageSerializer(ModelSerializer):
    """Used for serializing images list"""

    class Meta:
        model = Image
        fields = "__all__"


class CreateImageSerializer(AdminImageSerializer):
    """Used for creating a new image"""

    ...


class ImageSerializer(ModelSerializer):
    """Used for operations on user images"""

    class Meta:
        model = Image
        fields = ("id", "image_url", "created_at")


class UserSerializer(ModelSerializer):
    """Used for user retrieval"""

    class Meta:
        model = User
        fields = ("id", "username", "email")


class CurrentUserSerializer(ModelSerializer):
    """Used for current user retrieval"""

    class Meta:
        model = User
        fields = ("id", "username", "email", "last_login")
