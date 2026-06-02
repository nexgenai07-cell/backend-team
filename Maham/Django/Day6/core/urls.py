"""
URL configuration for core project.

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
# core/urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter

# Task 4 & Task 19: Global Router object create kar rahe hain [cite: 30, 31, 102, 111]
# DefaultRouter automatically hume ek API root page deta hai aur trailing slashes handle karta hai 
router = DefaultRouter()

# =========================================================================
# 1. CRM Application Routes (Task 1, 2, 18) [cite: 11, 15, 94]
# =========================================================================
from crm.views import StudentViewSet, TeacherViewSet, ClassroomViewSet

# Task 1: Student API ko ModelViewSet aur router urls ke sath register kiya [cite: 11, 12]
router.register(r'students', StudentViewSet, basename='student')

# Task 2: Teacher ViewSet ko router mei register kiya (GET, POST, PUT, DELETE automatic chalenge) [cite: 15, 16, 21]
router.register(r'teachers', TeacherViewSet, basename='teacher')

# Classroom ViewSet taake student filters proper kaam kar sakein
router.register(r'classrooms', ClassroomViewSet, basename='classroom')


# =========================================================================
# 2. E-commerce Application Routes (Task 3, 17) [cite: 22, 86]
# =========================================================================
from ecommerce.views import ProductViewSet, OrderViewSet

# Task 3: ProductViewSet ko register kiya jo standard CRUD handle karega [cite: 22, 29]
router.register(r'products', ProductViewSet, basename='product')

# Task 14: Order API nested serializer response check karne ke liye [cite: 74, 75]
router.register(r'orders', OrderViewSet, basename='order')


# =========================================================================
# Main URL Patterns Configuration
# =========================================================================
urlpatterns = [
    # Django ka apna built-in admin panel
    path('admin/', admin.site.urls),
    
    # Task 5: Hamein saare endpoints 'api/' prefix ke sath milenge (e.g., /api/products/) [cite: 35, 36]
    # include(router.urls) se saare automatic routes is path ke sath attach ho jayenge
    path('api/', include(router.urls)),
]

# =========================================================================
# Media URLs Routing (Task 10 & 11) [cite: 58, 60]
# =========================================================================
# Task 11: MEDIA_URL aur MEDIA_ROOT ko url configuration ke sath attach karna [cite: 64]
# Iske bagair browser ya Postman mei uploaded product/student images open nahi hongi
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)