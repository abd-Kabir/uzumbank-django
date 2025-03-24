from rest_framework import permissions


class LandingPage(permissions.BasePermission):
    """
    Allow users to GET requests
    """

    def has_permission(self, request, view):
        if view.action == 'list' or view.action == 'retrieve':
            return True
        return request.user.is_authenticated


class UzumbankPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.user
        return user.groups.filter(name__in=['UZUMBANK_WEBHOOK', 'ADMIN']).exists()
