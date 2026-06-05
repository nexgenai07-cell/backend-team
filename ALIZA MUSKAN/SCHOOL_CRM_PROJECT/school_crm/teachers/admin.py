from django.contrib import admin
from .models import Teacher

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    """
    Admin layout configuration specification for managing Faculty Teachers data records.
    """
    # Columns displayed in the listing grid sheet layout dashboard
    list_display = ('id', 'full_name', 'email', 'subject', 'salary')
    
    # Add clickable links to open the instance details sheet profile
    list_display_links = ('id', 'full_name')
    
    # Search input box configurations mapping criteria
    search_fields = ('full_name', 'email', 'subject')
    
    # Filter configurations settings pipeline
    list_filter = ('subject',)