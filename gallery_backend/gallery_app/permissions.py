from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """Permission that is used for giving users write access to their images and read only access to everyone else"""

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS or request.user.is_staff:
            return True
        else:
            return self.has_permission(request, view) and obj.user == request.user

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS or request.user.is_staff:
            return True

        return view.kwargs.get("user_pk") == str(request.user.id)


class IsAdminOrReadOnly(permissions.BasePermission):
    """Permission that is used for things you better not touch"""

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return request.user.is_staff
