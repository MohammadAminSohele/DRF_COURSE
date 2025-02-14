from rest_framework.permissions import BasePermission,SAFE_METHODS

class IsSuperUser(BasePermission):
    """ 
    Allows access only to admin users.
    """
    def has_permission(self,request,view):
        return bool(
            request.user.is_authenticated and request.user.is_superuser
        )
class IsStaffOrReadOnly(BasePermission):
    """ 
    The request is authenticated as a staff user, or is a read-only request.
    """
    def has_permission(self,request,view):
        return bool(
            request.method in SAFE_METHODS  or 
            request.user.is_authenticated and request.user.is_staff
        )
class IsAuthorOrReadOnly(BasePermission):
    """ 
    The request is authenticated as a superuser user, or author of objet is a read-only request.
    """
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return bool(
            # Allows access only to authenticated users. and:
            # get access to superuser
            request.user.is_authenticated and 
            request.user.is_superuser or
            # get access to author of objet
            obj.author==request.user
        )
class IsSuperUserOrStaffReadOnly(BasePermission):
    """ 
    The request is authenticated as a superuser user, or author of objet is a staff read-only request.
    """
    def has_permission(self,request,view):
        return bool(
            request.method in SAFE_METHODS and 
            request.user.is_authenticated and request.user.is_staff or 
            request.user.is_authenticated and request.user.is_superuser
        )