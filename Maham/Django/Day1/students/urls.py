from django.urls import path
from .views import (
    home_view, school_info_view, student_profile_view, 
    multiple_students_view, dynamic_student_view, classroom_view, 
    attendance_view, nested_school_view, about_view, result_view, dashboard_view
)

urlpatterns = [
    path('home', home_view),                                    # Task 3
    path('school-info', school_info_view),                      # Task 4
    path('student', student_profile_view),                      # Task 5
    path('students-list', multiple_students_view),              # Task 6 (Alag path name for list)
    path('student/<int:id>', dynamic_student_view),             # Task 7 (Dynamic Int)
    path('classroom', classroom_view),                          # Task 8
    path('attendance', attendance_view),                        # Task 9
    path('nested-school', nested_school_view),                  # Task 10
    path('about', about_view),                                  # Task 11
    path('result/<int:marks>', result_view),                    # Task 12 (Dynamic Int)
    path('dashboard', dashboard_view),                          # Task 13
]