from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter

# ✅ Import ViewSets
from students.views import StudentViewSet
from teachers.views import TeacherViewSet
from classrooms.views import ClassroomViewSet
from attendance.views import AttendanceViewSet

# ✅ JWT endpoints (direct token obtain/refresh)
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

# ✅ Router configuration
router = DefaultRouter()
router.register('students', StudentViewSet)
router.register('teachers', TeacherViewSet)
router.register('classrooms', ClassroomViewSet)
router.register('attendance', AttendanceViewSet)

# ✅ URL patterns
urlpatterns = [
    path('admin/', admin.site.urls),

    # Accounts app endpoints (register/login/profile/logout)
    path('api/', include('accounts.urls')),

    # CRUD endpoints for students, teachers, classrooms, attendance
    path('api/', include(router.urls)),

    # JWT endpoints (direct token obtain/refresh)
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

# ✅ Media files serve in development only
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
