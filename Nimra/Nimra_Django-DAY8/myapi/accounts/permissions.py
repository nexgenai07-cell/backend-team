# permissions.py
from rest_framework.permissions import BasePermission

# Sirf Admin role ko allow karega
class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'admin'

# Sirf Teacher role ko allow karega
class IsTeacher(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'teacher'

# Sirf Student role ko allow karega
class IsStudent(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'student'
