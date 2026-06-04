# Import Django admin panel functionality
from django.contrib import admin

# Import Django's built-in UserAdmin
# This gives default admin features for user management
from django.contrib.auth.admin import UserAdmin
# Import our custom Customer model
from .models import Customer
# Create custom admin configuration class
class CustomerAdmin(UserAdmin):

    # Fields shown while editing existing user
    fieldsets = UserAdmin.fieldsets + (

        ('Extra Information', {

            'fields': ('phone_number',)

        }),
    )

    # Fields shown while creating new user
    add_fieldsets = UserAdmin.add_fieldsets + (

        ('Extra Information', {

            'fields': ('phone_number',)

        }),
    )

admin.site.register(Customer, CustomerAdmin)