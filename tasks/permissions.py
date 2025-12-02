from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Read (GET) sab kar sakte hain.
    Write (PUT, PATCH, DELETE) sirf owner karega.
    """

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user
