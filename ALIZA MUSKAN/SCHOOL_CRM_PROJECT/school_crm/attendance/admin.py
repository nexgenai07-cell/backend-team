from django.contrib import admin
from .models import Attendance

@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    """
    Admin control records panel table manager workflow sheet tracking for Daily Attendance logs.
    """
    list_display = ('id', 'student', 'date', 'status')
    search_fields = ('student__full_name', 'student__roll_number')  # Double underscore to search into related Student fields
    list_filter = ('status', 'date')
    ordering = ('-date',)  # Shows the most recent attendance logs first on top