from django.urls import path
from .views import StudentListAPIView, TeacherListAPIView, StudentDetailAPIView, ClassListAPIView # StudentDetailAPIView add kiya

urlpatterns = [
    path('students', StudentListAPIView.as_view(), name='student-list'),
    path('teachers', TeacherListAPIView.as_view(), name='teacher-list'),
    
    # Task 10 & 11: Dynamic URL parameter <int:id> ke sath
    path('student/<int:id>', StudentDetailAPIView.as_view(), name='student-detail'),
    # Task 12 URL Path
    path('classes', ClassListAPIView.as_view(), name='class-list'),
]