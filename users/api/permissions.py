from rest_framework.permissions import BasePermission


class isDoctor(BasePermission):
    def has_permission(self, request, view):

        return bool(request.user.role == ("doctor") and request.user)


class isHospital(BasePermission):
    def has_permission(self, request, view):

        return bool(request.user.role == ("hospital") and request.user)
