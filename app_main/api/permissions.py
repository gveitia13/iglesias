from rest_framework import permissions


class IsOwnerOrAdminUser(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user or (request.user.is_superstar or request.user.role == '1')


