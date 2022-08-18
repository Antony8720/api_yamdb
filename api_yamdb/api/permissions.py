from rest_framework import permissions


class AdminOnlyPermission(permissions.BasePermission):
    """ Запросы POST, PATH, DELETE только у администратора, GET у всех"""

    def has_permission(self, request, view):
        return (
                request.method in permissions.SAFE_METHODS
                or request.user.is_authenticated and request.user.is_admin
        )


class SafeMethodOnlyPermission(permissions.BasePermission):
    """ Права доступа у Администратора"""

    def has_permission(self, request, view):
        return (request.method in permissions.SAFE_METHODS
                or request.user.is_authenticated and request.user.is_admin
        )