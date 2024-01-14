from rest_framework.permissions import BasePermission, AllowAny, IsAuthenticated


class IsEmployer(BasePermission):
    def has_permission(self, request, view):
        if request.method in ['POST']:
            return request.user.is_authenticated and request.user.is_employer
        return True

    def has_object_permission(self, request, view, obj):
        if request.method in ['PUT', 'PUTCH', 'DELETE']:
            return request.user == obj.who_created
        return True

class PermissionMixin:
    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            self.permission_classes = [AllowAny]
        else:
            self.permission_classes = [IsEmployer]
        return super().get_permissions()