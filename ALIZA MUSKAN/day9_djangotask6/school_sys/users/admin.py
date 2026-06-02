from django.contrib import admin
from .models import Student,Teacher,Classroom
# task1
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    """
    Admin configuration for Student model.
    """

    list_display = ['id', 'name', 'email', 'age']
     # Search functionality in admin
    search_fields = ('name', 'email')
    # Filter sidebar in admin panel
    list_filter = ('age',)
# task2
@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    """
    Teacher Admin Configuration
    """
    list_display = ('id', 'name', 'subject', 'email', 'experience')
    # Search box in admin panel
    search_fields = ('name', 'subject', 'email')
    # Filter sidebar in admin panel
    list_filter = ('subject', 'experience')
    # task3
@admin.register(Classroom)
class ClassAdmin(admin.ModelAdmin):
    list_display = ('name', 'teacher')