from rest_framework.permissions import BasePermission

class IsOwner(BasePermission):
    # это наш пермишн который мы сами написали
    def has_object_permission(self, request, view, obj):
        return request.user == obj.user