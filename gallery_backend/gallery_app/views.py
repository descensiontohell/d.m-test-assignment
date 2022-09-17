from django.contrib.auth.models import User
from django.utils.decorators import method_decorator
from rest_framework import status
from rest_framework import viewsets
from rest_framework import views
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema

from .models import Image
from .serializers import (
    AdminImageSerializer,
    CreateImageSerializer,
    CurrentUserSerializer,
    ImageSerializer,
    UserSerializer,
)
from .permissions import IsOwnerOrReadOnly, IsAdminOrReadOnly


class AdminImageView(views.APIView):
    """Allows admin to list all the images in the system and delete all of them if needed"""

    permission_classes = [IsAdminUser]

    @swagger_auto_schema(
        operation_summary="Get all images [admin]",
        operation_description="Returns a list of all images in the application",
    )
    def get(self, request, *args, **kwargs):
        images = Image.objects.all()
        serializer = AdminImageSerializer(images, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_summary="Delete all images [admin]",
        operation_description="Deletes all the images in the database",
    )
    def delete(self, request, *args, **kwargs):
        Image.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@method_decorator(
    name="list",
    decorator=swagger_auto_schema(
        operation_summary="Get all users", operation_description="Returns a list of all users in the system"
    ),
)
@method_decorator(
    name="update",
    decorator=swagger_auto_schema(
        operation_summary="Update user data", operation_description="Allows admin to update user fields"
    ),
)
@method_decorator(
    name="retrieve",
    decorator=swagger_auto_schema(
        operation_summary="Get user by id", operation_description="Returns user object with given id if exists"
    ),
)
@method_decorator(
    name="partial_update",
    decorator=swagger_auto_schema(
        operation_summary="Updates user", operation_description="Updates given fields of a user if exists"
    ),
)
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminOrReadOnly]
    http_method_names = ["get", "patch"]


@method_decorator(
    name="list",
    decorator=swagger_auto_schema(
        operation_summary="Get user images", operation_description="Returns a list of images that belong to given user"
    ),
)
@method_decorator(
    name="create",
    decorator=swagger_auto_schema(
        operation_summary="Create image", operation_description="Adds image to the current user"
    ),
)
@method_decorator(
    name="retrieve",
    decorator=swagger_auto_schema(
        operation_summary="Get image by id",
        operation_description="Returns image with given id if it belongs to given user",
    ),
)
@method_decorator(
    name="partial_update",
    decorator=swagger_auto_schema(
        operation_summary="Update image", operation_description="Updates listed fields of an image"
    ),
)
@method_decorator(
    name="destroy",
    decorator=swagger_auto_schema(
        operation_summary="Deletes the image", operation_description="Deletes image with given image id and user id"
    ),
)
class ImageViewSet(viewsets.ModelViewSet):
    permission_classes = [IsOwnerOrReadOnly]
    http_method_names = ["get", "post", "patch", "delete"]

    def get_queryset(self):
        return Image.objects.filter(user=self.kwargs.get("user_pk"))

    def get_serializer_class(self):
        # Image serializer should have user_id field on create
        if self.action == "create":
            return CreateImageSerializer
        else:
            return ImageSerializer

    def create(self, request, *args, **kwargs):
        # Gets current <user_id> from path as resource owner
        request.data["user"] = kwargs.get("user_pk")
        return super().create(request, *args, **kwargs)


class CurrentUserView(viewsets.ReadOnlyModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = CurrentUserSerializer

    @swagger_auto_schema(operation_summary="Get current user", operation_description="Returns current user object")
    def retrieve(self, request, *args, **kwargs):
        user = request.user
        serializer = self.get_serializer(user)
        return Response(serializer.data)
