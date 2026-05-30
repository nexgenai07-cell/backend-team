from django.urls import path

from .views import (
    SellerRegisterView,
    SellerLoginView,
    SellerDashboardView
)

urlpatterns = [

    path(
        'seller/register/',
        SellerRegisterView.as_view()
    ),

    path(
        'seller/login/',
        SellerLoginView.as_view()
    ),

    path(
        'seller/dashboard/',
        SellerDashboardView.as_view()
    ),
]