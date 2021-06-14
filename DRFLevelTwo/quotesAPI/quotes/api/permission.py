from rest_framework import permissions


class IsAdminUserOrReadOnly(permissions.IsAdminUser):

    def has_permission(self, request, view):
        is_admin = super().has_permission(request,view)
    
        SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS')
        return request.method in SAFE_METHODS or is_admin