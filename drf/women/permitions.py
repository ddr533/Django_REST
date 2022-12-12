from rest_framework import permissions


class IsAdminOrReadOnly(permissions.BasePermission):  # чтение для всех, удалять может только админ
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:  # запрос из GET, HEAD, OPTIONS
            return True

        return bool(request.user and request.user.is_staff)  # проверка на админа (из ISAdminUser)


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user == request.user
