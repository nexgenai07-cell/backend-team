# Import Django admin panel
from django.contrib import admin
# Import path and include
from django.urls import path, include
urlpatterns = [
    # Admin panel route
    path('admin/', admin.site.urls),
    # Customer authentication APIs
    path( 'api/customers/',include('customers.urls') ),
]