from django.urls import path

from .views import (

    AddProductView,

    ProductListView,

    UpdateProductView,

    DeleteProductView
)

urlpatterns = [

    path(
        'add/',
        AddProductView.as_view()
    ),

    path(
        'list/',
        ProductListView.as_view()
    ),

    path(
        'update/<int:pk>/',
        UpdateProductView.as_view()
    ),

    path(
        'delete/<int:pk>/',
        DeleteProductView.as_view()
    ),
]