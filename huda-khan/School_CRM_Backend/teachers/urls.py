from django.urls import path
from .views import TeacherListCreateView

urlpatterns = [
    path('teachers/', TeacherListCreateView.as_view()),
]