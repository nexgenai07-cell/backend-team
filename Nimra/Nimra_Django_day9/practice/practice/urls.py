"""
URL configuration for practice project.

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
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static   # 👈 media serve karne ke liye import
from rest_framework.routers import DefaultRouter # DefaultRouter = automatically generates URL patterns for our viewsets
from intern.views import StudentViewSet, TeacherViewSet, ProductViewSet,OrderViewSet # import the StudentViewSet we created in intern/views.py
router = DefaultRouter()
router.register(r'students', StudentViewSet)
router.register(r'teachers', TeacherViewSet)   # ✅ Teacher route added
router.register(r'products', ProductViewSet)   # ✅ Product route added
router.register(r'orders', OrderViewSet)   # 👈 Order route add karo
urlpatterns = [
    path('admin/', admin.site.urls),
      path('', include(router.urls)), # include the router URLs at the root URL
]
# 👇 Ye line sirf project‑level urls.py me likhni hai
# Ye Django ko batata hai ke agar koi request /media/... URL pe aaye
# to usko MEDIA_ROOT folder se file serve karni hai.
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
