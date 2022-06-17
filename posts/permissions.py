from rest_framework import permissions


class IsAuthorReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:  # read permission
            return True
        return obj.author == request.user               # write permission
