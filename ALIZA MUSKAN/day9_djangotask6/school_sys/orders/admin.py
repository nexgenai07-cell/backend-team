
from django.contrib import admin
from .models import Order
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    """
    Admin configuration for Order model.
    """
    list_display = [
        'id',
        'customer',
        'created_at'
    ]
   