"""
URL configuration for school_crm project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from students.views import home_view, school_info_view,student,multiple_students_view,dynamic_student_view,classroom,attendance_view,nested_school_view,about_view,result_view,dashboard_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home_view, name='home'),
    path('school-info/', school_info_view, name='school_info'),
    path('student/', student, name='student'),
    path('students/', multiple_students_view, name='multiple_students'),
    path('student/<int:student_id>/', dynamic_student_view, name='dynamic_student'),
    path('classroom/', classroom, name='classroom'),
    path('attendance/', attendance_view, name='attendance_status'),
    path('school-detail/', nested_school_view, name='nested_school_detail'),
    path('about/', about_view, name='project_about'),
    path('result/<int:marks>/', result_view, name='result_check'),
    path('dashboard/', dashboard_view, name='school_dashboard'),
]
