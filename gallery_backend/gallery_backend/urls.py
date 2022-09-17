"""gallery_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import SimpleRouter
from rest_framework_nested import routers

from gallery_app.views import CurrentUserView, ImageViewSet, UserViewSet, AdminImageView
)

router = SimpleRouter()
router.register(r"users", UserViewSet)

images_router = routers.NestedSimpleRouter(router, r"users", lookup="user")
images_router.register(r"images", ImageViewSet, basename="user-images")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("images/", AdminImageView.as_view()),
    path("accounts/", include("rest_registration.api.urls")),
    path("users/me/", CurrentUserView.as_view({"get": "list"})),
    path(r"", include(router.urls)),
    path(r"", include(images_router.urls)),
]

urlpatterns += router.urls
