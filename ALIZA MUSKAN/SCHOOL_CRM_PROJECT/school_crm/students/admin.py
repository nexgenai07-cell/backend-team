from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    """
    Admin monitoring control management panel setup configuration for Student profiles.
    """
    list_display = ('id', 'roll_number', 'full_name', 'email', 'age', 'classroom')
    list_display_links = ('id', 'roll_number', 'full_name')
    search_fields = ('full_name', 'roll_number', 'email')
    list_filter = ('classroom', 'age')