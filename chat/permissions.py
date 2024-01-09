from rest_framework import permissions

class IsChatParticipant(permissions.BasePermission):
    """
    Пользователь может читать сообщения только в том чате, в котором он участвует.
    """

    def has_object_permission(self, request, view, obj):
        return request.user == obj.participant1 or request.user == obj.participant2
