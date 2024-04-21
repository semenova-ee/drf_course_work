from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    message = 'Доступ запрещен'

    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user


class IsModerator(BasePermission):
    message = 'Доступ запрещен'

    def has_permission(self, request, view):
        if request.user.is_staff:
            return True
        return False
