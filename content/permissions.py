from rest_framework.permissions import BasePermission

# class IsAuthor(BasePermission):
#     def has_object_permission(self, request, view, obj):
#         return request.user.is_authenticated and obj.author == request.user

class IsCommenterAuthorized(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.is_authenticated