from django.urls import path

from .views import (
    RegisterView,
    LoginView,
    ProfileView,
    AllUsersView
)

urlpatterns = [
    path(  'register/',  RegisterView.as_view() ),
    path(  'login/',  LoginView.as_view()),
    path( 'profile/', ProfileView.as_view() ),
    path( 'all-users/', AllUsersView.as_view()),
]