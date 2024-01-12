from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in ['GET', 'PUT', 'PATCH', 'DELETE']:
            return True
        return obj.user == request.user
