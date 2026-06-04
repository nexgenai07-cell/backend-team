from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StudentViewSet,TeacherViewSet,ClassroomViewSet
# Router automatically generates URLs for ViewSet
router = DefaultRouter()

# Register Student API endpoints
router.register(
    r'students',        # URL prefix
    StudentViewSet,     # ViewSet class
    basename='student'  # Name reference
)
# Teacher API (ADVANCED)
router.register(r'teachers', TeacherViewSet, basename='teacher')
router.register(r'classrooms', ClassroomViewSet, basename='classroom')
urlpatterns = [
    path('', include(router.urls)),
]