from django.contrib import admin

# Register your models here.
from .models import Student,Teacher,Class

admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Class)