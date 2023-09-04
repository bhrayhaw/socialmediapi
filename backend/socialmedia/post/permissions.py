#custom permissions for posts
from rest_framework import permissions
    
class IsOwnerOrReadOnlyPost(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """    
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_authenticated
    
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.post.user == request.user