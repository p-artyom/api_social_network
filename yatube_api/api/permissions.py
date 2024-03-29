from rest_framework import permissions


class AuthorCanEditAndDelete(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        del view
        return (
            obj.author == request.user
            or request.method in permissions.SAFE_METHODS
        )
