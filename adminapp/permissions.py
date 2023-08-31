from rest_framework import permissions

class IsAllowedToWrite(permissions.BasePermission):
    '''class will define the permissions'''
    def has_permission(self, request, view):
        return ((request.user.is_authenticated))