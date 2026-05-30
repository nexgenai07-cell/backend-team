# Import Django path function
from django.urls import path

# Import API views
from .views import (
    CustomerRegisterAPIView,
    CustomerLoginAPIView,
    CustomerProfileAPIView,
    CustomerUpdateProfileAPIView,
)


# All customer authentication routes
urlpatterns = [

    path( 'register/', CustomerRegisterAPIView.as_view() ),
    path('login/', CustomerLoginAPIView.as_view()),
    path( 'profile/', CustomerProfileAPIView.as_view()),   
    path('update-profile/',CustomerUpdateProfileAPIView.as_view()),
]