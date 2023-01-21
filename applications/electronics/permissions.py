from rest_framework import permissions
from rest_framework.permissions import SAFE_METHODS


class IsSellerOrReadOnly(permissions.BasePermission):
    # CREATE, LIST
    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        return request.user.is_seller and request.user.is_authenticated

    # RETRIEVE, UPDATE, DELETE
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return request.user.is_authenticated and (
                (request.user == obj.user and request.user.is_seller) or request.user.is_staff)
