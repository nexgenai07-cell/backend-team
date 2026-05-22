from django.db import models
from django.contrib.auth.models import AbstractUser

# ✅ CustomUser model jo default Django User ko extend karta hai
class CustomUser(AbstractUser):
    # Role choices define kiye (sirf 3 roles allowed honge)
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('teacher', 'Teacher'),
        ('student', 'Student'),
    )

    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='student')
    # User ka role (admin, teacher, student) — default student rakha hai

    phone = models.CharField(max_length=15, blank=True, null=True)
    # Optional phone number field

    address = models.CharField(max_length=255, blank=True, null=True)
    # Optional address field

    def __str__(self):
        return self.username
        # Admin panel mein readable output ke liye username return karega
