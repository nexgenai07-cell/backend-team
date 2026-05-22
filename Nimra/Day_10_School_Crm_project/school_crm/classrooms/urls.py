from rest_framework.routers import DefaultRouter
from .views import ClassroomViewSet   # apne views.py se ClassroomViewSet import kiya

# ✅ Router DRF ka shortcut hai jo automatically CRUD endpoints banata hai
router = DefaultRouter()

# ✅ ClassroomViewSet ko register kiya 'classrooms' prefix ke sath
# Isse tumhe endpoints milenge: /classrooms/, /classrooms/{id}/
router.register('classrooms', ClassroomViewSet)

# ✅ urlpatterns mein router ke URLs add kiye
urlpatterns = router.urls
