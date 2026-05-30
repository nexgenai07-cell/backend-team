from django.urls import path

from .views import ( PlaceOrderView, UserOrdersView, AllOrdersView)

urlpatterns = [
    path(  'place/',PlaceOrderView.as_view() ),

    path(  'my-orders/', UserOrdersView.as_view()),

    path('all-orders/',AllOrdersView.as_view()  ),
]