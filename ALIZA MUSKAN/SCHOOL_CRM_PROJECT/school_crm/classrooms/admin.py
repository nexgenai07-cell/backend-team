from django.contrib import admin
from .models import Classroom

@admin.register(Classroom)
class ClassroomAdmin(admin.ModelAdmin):
    """
    Admin dashboard sheet workspace tracking layout configuration parameters for Classrooms.
    """
    list_display = ('id', 'class_name', 'section', 'room_number', 'class_teacher')
    list_display_links = ('id', 'class_name')
    search_fields = ('class_name', 'section', 'room_number')
    list_filter = ('class_name', 'section')