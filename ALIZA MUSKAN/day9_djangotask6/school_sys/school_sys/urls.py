from django.contrib import admin
from django.urls import path, include
from django.conf import settings # Import settings to access DEBUG, MEDIA_URL, and MEDIA_ROOT
from django.conf.urls.static import static  # Import static helper function to serve development files
urlpatterns = [
    path('admin/', admin.site.urls),

    # Include  app APIs
    path('api/', include('users.urls')),
    path('api/', include('products.urls')),
    path('api/',include('orders.urls')),
]

# Check if the project is running in local development mode (DEBUG = True)
# Django does not serve media files in production, so this configuration is only for local testing

if settings.DEBUG:
    # Append the media files URL pattern to the existing urlpatterns
    # It maps the browser request (MEDIA_URL) to the actual folder on your computer (MEDIA_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)