from django.contrib import admin
from .models import Student

# Student model ko admin panel mein register kiya taake hum wahan se data add/delete kar sakein
admin.site.register(Student)