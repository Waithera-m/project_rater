from rest_framework.permissions import SAFE_METHODS, BasePermission

class IsAuthenticatedOrReadOnly(BasePermission):
    """
    class allows authenticated users to interact with the api
    """
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        else:
            return request.user.is_staff