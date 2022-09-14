from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.response import Response


from .models import Image
from .serializers import CurrentUserSerializer, ImageSerializer, UserSerializer, UserImagesSerializer


class ImagesViewSet(ModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = Image.objects.all()
    serializer_class = ImageSerializer


class UsersViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer  # TODO отключить круды всем кроме админа


class CurrentUserViewSet(ReadOnlyModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = CurrentUserSerializer

    def list(self, request, *args, **kwargs):
        user = request.user
        serializer = self.get_serializer(user)
        return Response(serializer.data)


class UserImagesViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]

    def list(self, *args, **kwargs):
        user_id = kwargs["user_id"]
        queryset = Image.objects.filter(user_id=user_id)
        serializer = UserImagesSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, *args, **kwargs):
        ...  # TODO сделать круды для картинок


class UserSingleImageViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]

    def list(self, *args, **kwargs):
        user_id = kwargs["user_id"]
        image_id = kwargs["image_id"]

        # try:
        queryset = Image.objects.get_object_or_404(user_id=user_id, id=image_id)
        # except Image.DoesNotExist:
        #     return Response(status=status.HTTP_404_NOT_FOUND, data={"detail": "Not found."})

        serializer = UserImagesSerializer(queryset, many=False)
        return Response(serializer.data)
