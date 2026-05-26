from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    StudentDetailAPIView, StudentListAPIView, 
    TeacherViewSet, ClassroomViewSet, 
    AttendanceViewSet, ResultViewSet, ProductViewSet, CartViewSet,
    OrderViewSet
)

router = DefaultRouter()
router.register(r'teachers', TeacherViewSet, basename='teacher')
router.register(r'classrooms', ClassroomViewSet, basename='classroom')
router.register(r'attendance', AttendanceViewSet, basename='attendance')
router.register(r'results', ResultViewSet, basename='result')
router.register(r'products', ProductViewSet, basename='product')
router.register(r'cart', CartViewSet, basename='cart')
router.register(r'orders', OrderViewSet, basename='order')

urlpatterns = [
    path('student/<int:id>/', StudentDetailAPIView.as_view(), name='student-detail'),
    path('students/', StudentListAPIView.as_view(), name='student-list'),
    path('', include(router.urls)),
]