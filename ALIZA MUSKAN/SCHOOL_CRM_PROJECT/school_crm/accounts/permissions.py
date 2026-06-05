# accounts/permissions.py
from rest_framework.permissions import BasePermission

class IsAdminUserRole(BasePermission):
    """
    Custom permission to allow access only to users with the ADMIN role.
    """
    def has_permission(self, request, view):
        # Check if user is authenticated and has the ADMIN role attribute
        return bool(request.user and request.user.is_authenticated and request.user.is_admin)


class IsTeacherUserRole(BasePermission):
    """
    Custom permission to allow access only to users with the TEACHER role.
    """
    def has_permission(self, request, view):
        # Check if user is authenticated and has the TEACHER role attribute
        return bool(request.user and request.user.is_authenticated and request.user.is_teacher)


class IsStudentUserRole(BasePermission):
    """
    Custom permission to allow access only to users with the STUDENT role.
    """
    def has_permission(self, request, view):
        # Check if user is authenticated and has the STUDENT role attribute
        return bool(request.user and request.user.is_authenticated and request.user.is_student)