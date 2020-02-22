from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """
        Allow User To Edit their Own Profiles 
    """

    def has_object_permission(self, request, view, obj):
        """
            Check User is trying to Edit their own Profiles
        """
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id

