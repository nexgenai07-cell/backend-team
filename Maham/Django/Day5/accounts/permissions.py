from rest_framework.permissions import BasePermission

class IsAdminRole(BasePermission):
    """Sirf Admin users ko access allow karega"""
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and request.user.role == 'admin'

class IsTeacherRole(BasePermission):
    """Sirf Teacher users ko access allow karega"""
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and request.user.role == 'teacher'

class IsStudentRole(BasePermission):
    """Sirf Student users ko access allow karega"""
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and request.user.role == 'student'
    
class IsSellerRole(BasePermission):
    """Sirf Seller users ko access allow karega"""
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and request.user.role == 'seller'

class IsCustomerRole(BasePermission):
    """Sirf Customer users ko access allow karega"""
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and request.user.role == 'customer'