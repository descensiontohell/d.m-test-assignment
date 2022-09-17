from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework import generics
from rest_framework import viewsets
from rest_framework import views
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response

from .models import Image
from .serializers import CurrentUserSerializer, ImageSerializer, UserSerializer, UserImagesSerializer
from .permissions import IsOwnerOrReadOnly, IsAdminOrReadOnly


class AdminImageView(views.APIView):
    permission_classes = [IsAdminUser]

    def get(self, request, *args, **kwargs):
        images = Image.objects.all()
        serializer = ImageSerializer(images, many=True)
        return Response(serializer.data)

    def delete(self, request, *args, **kwargs):
        Image.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminOrReadOnly]
    http_method_names = ["get", "patch"]


class ImageViewSet(viewsets.ModelViewSet):
    serializer_class = ImageSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get_queryset(self):
        return Image.objects.filter(user=self.kwargs.get("user_pk"))

    def create(self, request, *args, **kwargs):
        request.data["user"] = self.request.user.id
        return super().create(request, *args, **kwargs)


class CurrentUserView(viewsets.ReadOnlyModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = CurrentUserSerializer

    def retrieve(self, request, *args, **kwargs):
        user = request.user
        serializer = self.get_serializer(user)
        return Response(serializer.data)
