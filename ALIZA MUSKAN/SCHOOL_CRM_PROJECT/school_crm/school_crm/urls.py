from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.http import HttpResponse
from django.http import JsonResponse
def home(request):
    return JsonResponse({
        "message": "School CRM API is running 🚀"
    })
# Import views from accounts app
from accounts.views import RegisterView, UserProfileView

# Import ViewSets from management apps
from teachers.views import TeacherViewSet
from classrooms.views import ClassroomViewSet
from students.views import StudentViewSet
from attendance.views import AttendanceViewSet

# 1. Initialize DefaultRouter for management apps
router = DefaultRouter()
router.register(r'teachers', TeacherViewSet, basename='teacher')
router.register(r'classrooms', ClassroomViewSet, basename='classroom')
router.register(r'students', StudentViewSet, basename='student')
router.register(r'attendance', AttendanceViewSet, basename='attendance')

urlpatterns = [
     path('', home), 
    path('admin/', admin.site.urls),
    
    # 2. Manual Authentication Endpoints (Matching the exact PDF requirement specification)
    path('api/register/', RegisterView.as_view(), name='auth_register'),
    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/profile/', UserProfileView.as_view(), name='user_profile'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    # 3. Automatic ViewSet Routers for all remaining management systems
    path('api/', include(router.urls)),
]

# Serve media files locally during the development environment phase
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
def favicon(request):
    return HttpResponse(status=204)

urlpatterns += [
    path('favicon.ico', favicon),
    path('favicon.png', favicon),
]
