from django.urls import path

from .views import (

    AddToCartView,

    ViewCartView,

    RemoveFromCartView
)

urlpatterns = [

    path(
        'add/',
        AddToCartView.as_view()
    ),

    path(
        'view/',
        ViewCartView.as_view()
    ),

    path(
        'remove/<int:pk>/',
        RemoveFromCartView.as_view()
    ),
]