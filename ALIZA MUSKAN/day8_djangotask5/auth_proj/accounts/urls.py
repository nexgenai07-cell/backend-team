from django.urls import path
from .views import (
    StudentRegisterView,
    StudentProfileView,
    TeacherRegisterView,
    TeacherDashboardView,
    StudentDashboardView,
    AdminDashboardView,
    AdminProtectedView,
    ChangePasswordView,
    UpdateProfileView
)

urlpatterns = [
    path('register/', StudentRegisterView.as_view()),
    path('profile/', StudentProfileView.as_view()),
    path('teacher/register/', TeacherRegisterView.as_view()),
    path('teacher/dashboard/', TeacherDashboardView.as_view()),
    path('student/dashboard/', StudentDashboardView.as_view()),
    path('admin/dashboard/', AdminDashboardView.as_view()),
    # task8 
    path('admin/protected/', AdminProtectedView.as_view()),
    # task 9
    path('change-password/', ChangePasswordView.as_view()),
    # task 10
    path('update-profile/', UpdateProfileView.as_view()),
]