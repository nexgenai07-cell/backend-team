from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

# Importing the API views cleanly from the integrations app
from integrations.views import UserProfileListAPIView, PaymentListAPIView, AiRequestListAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # API Endpoints for Postman Testing
    path('api/user-profiles/', UserProfileListAPIView.as_view(), name='api-user-profiles'),
    path('api/payments/', PaymentListAPIView.as_view(), name='api-payments'),
    path('api/ai-requests/', AiRequestListAPIView.as_view(), name='api-ai-requests'),
]

# Media URL routing for local/Cloudinary fallback handling
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)