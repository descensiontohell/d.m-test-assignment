from django.contrib.auth.models import User
from drf_yasg.utils import serializers
from rest_framework.serializers import ModelSerializer

from .models import Image
from .utils import is_url_image


class AdminImageSerializer(ModelSerializer):
    """Used for serializing images list"""

    class Meta:
        model = Image
        fields = "__all__"


class CreateImageSerializer(AdminImageSerializer):
    """Used for creating a new image"""

    def validate_image_url(self, value: str):
        if is_url_image(value):
            return value
        raise serializers.ValidationError("image_url is not a valid image url")


class ImageSerializer(CreateImageSerializer):
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
