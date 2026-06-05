# Importing Django's path function to define URL patterns for the application
from django.urls import path

# Importing SimpleJWT views to handle authentication token generation and refreshing
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

# Importing custom views created in your views.py file for registration and profile management
from .views import RegisterView, UserProfileView

urlpatterns = [
    # Registration endpoint: Maps to RegisterView to handle new user sign-ups
    path('register/', RegisterView.as_view(), name='auth_register'),
    
    # Login endpoint: Maps to TokenObtainPairView. 
    # Takes 'username' and 'password' to verify credentials and returns an Access Token and a Refresh Token.
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    
    # Token Refresh endpoint: Maps to TokenRefreshView.
    # Takes a valid 'refresh' token to generate a brand new 'access' token without forcing the user to log in again.
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    # Authenticated User Profile endpoint: Maps to UserProfileView.
    # Used to fetch or update the logged-in user's data (requires a valid Access Token in the request header).
    path('profile/', UserProfileView.as_view(), name='user_profile'),
]