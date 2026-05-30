from django.db import models
from django.contrib.auth.models import AbstractUser
class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('teacher', 'Teacher'),
        ('student', 'Student'),
    )
    # User role
    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES
    )
    # Extra field
    phone_number = models.CharField(
        max_length=15
    )
    def __str__(self):
        return self.username