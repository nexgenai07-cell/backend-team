from django.contrib import admin
from .models import User


# Register custom user model in admin panel
admin.site.register(User)