from django.urls import path
from .views import StudentListView, StudentCreateView, TeacherAPIView, StudentDetailAPIView, ClassAPIView

urlpatterns = [
    path('', StudentListView.as_view(), name='students-list'),
    path('add/', StudentCreateView.as_view(), name='student-create'),
    path('teachers/', TeacherAPIView.as_view(), name='teacher_api'),
    path('student/<int:pk>/', StudentDetailAPIView.as_view(), name='student_detail'),
    path('classes/', ClassAPIView.as_view(), name='class_api'),
]


