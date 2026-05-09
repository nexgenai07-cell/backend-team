from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home),
    path('school-info/', views.school_info),
    path('student/', views.student_profile),
    path('students/', views.multiple_students),
    path('result/<int:marks>/', views.result),
    path('student/<int:id>/', views.student_detail),
    path('dashboard/', views.dashboard),
]