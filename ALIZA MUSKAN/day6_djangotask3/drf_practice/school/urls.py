from django.urls import path

from .views import StudentAPIView,TeacherAPIView, StudentDetailAPIView,ClassAPIView


urlpatterns = [

    path('students/', StudentAPIView.as_view() ),
    path('teachers/', TeacherAPIView.as_view()),
    path('student/<int:id>/', StudentDetailAPIView.as_view()),
    path('classes/', ClassAPIView.as_view()),
]