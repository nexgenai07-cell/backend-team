from django.contrib.auth.models import AbstractUser
from django.db import models

# ========================================================
# CUSTOM USER MODEL (With Custom Roles)
# ========================================================
class User(AbstractUser):
    # PDF ke mutabiq 3 roles define kiye hain [cite: 41]
    ROLE_CHOICES = (
        ('ADMIN', 'Admin'),
        ('TEACHER', 'Teacher'),
        ('STUDENT', 'Student'),
    )
    
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='ADMIN')
    email = models.EmailField(unique=True) # Email unique hona chahiye login ke liye

    # Jab username field email ban jaye to login email se hota hai
    REQUIRED_FIELDS = ['username', 'role']
    USERNAME_FIELD = 'email'

    def __str__(self):
        return f"{self.email} ({self.role})"