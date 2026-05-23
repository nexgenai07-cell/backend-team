from django.urls import path
from .views import school_info,student_profile

urlpatterns = [
    path('school-info/', school_info, name='school_info'),
    path('student/<int:student_id>/',student_profile, name='student_profile'),
]
