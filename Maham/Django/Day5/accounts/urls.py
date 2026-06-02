from django.urls import path
from .views import (
    RegisterView, LoginView, ProfileView, 
    StudentProfileView, TeacherDashboardView, AdminOnlyView,
    ChangePasswordView, UpdateProfileView,
    ProductListCreateView, CartAPIView, OrderAPIView  # <--- Import kiye
)

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('student/profile/', StudentProfileView.as_view(), name='student-profile'),
    path('teacher/dashboard/', TeacherDashboardView.as_view(), name='teacher-dashboard'),
    path('admin/protected/', AdminOnlyView.as_view(), name='admin-protected'),
    path('change-password/', ChangePasswordView.as_view(), name='change-password'),
    path('update-profile/', UpdateProfileView.as_view(), name='update-profile'),
    
    # New E-commerce Endpoints
    path('products/', ProductListCreateView.as_view(), name='products'),
    path('cart/', CartAPIView.as_view(), name='cart'),
    path('orders/', OrderAPIView.as_view(), name='orders'),
]