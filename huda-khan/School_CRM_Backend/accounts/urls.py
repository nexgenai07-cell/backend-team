# Import path
from django.urls import path

# Import views
from .views import RegisterView, ProfileView

# Import JWT login view
from rest_framework_simplejwt.views import TokenObtainPairView


urlpatterns = [

    # Register API
    path('register/', RegisterView.as_view()),

    # Login API (JWT)
    path('login/', TokenObtainPairView.as_view()),

    # Profile API
    path('profile/', ProfileView.as_view()),
]