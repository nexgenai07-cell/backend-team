from django.urls import path
from .views import ClassroomListCreateView

urlpatterns = [
    path('classrooms/', ClassroomListCreateView.as_view()),
]