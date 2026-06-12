from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Route for the built-in Django Admin interface
    path('admin/', admin.site.urls),
]

# Serve media files (uploads) during development
# Note: This is only required when DEBUG is True. In production, 
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,          # The URL prefix for media files (e.g., /media/)
        document_root=settings.MEDIA_ROOT  # The actual file system path where files are stored
    )