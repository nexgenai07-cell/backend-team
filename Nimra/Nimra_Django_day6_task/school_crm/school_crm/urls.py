"""
URL configuration for school_crm project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.urls import path, include   # include use karte hain app ke urls connect karne ke liye
from students.views import StudentListView   # import karo
urlpatterns = [
   
    path('admin/', admin.site.urls),          # Admin panel route
    path('students/', include('students.urls')),  # Students app routes
    path('', StudentListView.as_view(), name='home'),   # root par students list

]
