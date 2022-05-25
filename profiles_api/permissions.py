from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """Allow a user to edit their own profile only"""

    def has_object_permission(self, request, view, obj):
        """Check user is trying to eedit their own profile"""
        if request.method in permissions.SAFE_METHODS:
            return True
            
        return obj.id == request.user.id