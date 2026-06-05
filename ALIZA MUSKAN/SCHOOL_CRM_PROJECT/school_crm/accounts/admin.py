from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    """
    Custom Admin interface management config for CustomUser Model.
    Extends standard UserAdmin to include role-based access fields and profile info.
    """
    # Configuration columns to display in the admin table list layout view
    list_display = ('username', 'email', 'role', 'phone_number', 'is_staff', 'is_active')
    
    # Adding filters on the right sidebar for quick data navigation
    list_filter = ('role', 'is_staff', 'is_active')
    
    # Fieldsets configuration to structure the user detail edit page layout
    fieldsets = UserAdmin.fieldsets + (
        ('Extra Profile Specifications', {
            'fields': ('role', 'phone_number', 'profile_picture'),
        }),
    )
    
    # Fieldsets configuration for creating a new user via admin panel
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Extra Profile Specifications', {
            'fields': ('role', 'phone_number', 'profile_picture'),
        }),
    )

# Register the CustomUser model with its dedicated Admin configuration layout
admin.site.register(CustomUser, CustomUserAdmin)