from django .urls import path
from . import views
urlpatterns=[
                    path('home/',views.home,name='home'),
                    path('school-info/',views.school_info,name='school-info'),
                    path('student/',views.student_profile,name='student-profile'),
                    path('student/<int:id>/',views.student_detail,name='student-detail'),
                    path('attendance/',views.attandance,name='attendance'),
                    path('result/<int:marks>/', views.result, name='result'),
                    path('students-list/', views.multiple_students, name='multiple_students'),
                    path('classroom/', views.classroom, name='classroom'),
                    path('nested/', views.nested_school, name='nested_school'),
                    path('about/', views.about, name='about'),
                    path('dashboard/', views.dashboard, name='dashboard'),





]

