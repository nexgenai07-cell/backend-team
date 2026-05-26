from django.contrib import admin
from .models import Student, Teacher, Class

# Task 5: Registering models so they appear in the Admin Panel
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Class)  # Yeh line Class model ko admin dashboard par show karegi