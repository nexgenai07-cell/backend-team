from django.urls import path
from accounts.views import RegisterView, LoginView, ProfileView

# ✅ Accounts app ke endpoints define kiye
urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),   # User registration endpoint
    path('login/', LoginView.as_view(), name='login'),            # User login endpoint
    path('profile/', ProfileView.as_view(), name='profile'),      # User profile endpoint
]
