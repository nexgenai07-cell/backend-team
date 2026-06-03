from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ClassroomViewSet

# Simple DRF Router register karna
router = DefaultRouter()
router.register(r'classrooms', ClassroomViewSet, basename='classroom')

urlpatterns = [
    path('', include(router.urls)), # Router ki saari URLs register ho gayi hain
]