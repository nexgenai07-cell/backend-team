# Import AbstractUser to customize default Django user model
from django.contrib.auth.models import AbstractUser

# Import models for creating database fields
from django.db import models


# Custom User Model extending Django's built-in AbstractUser
class User(AbstractUser):

    # Role choices for different types of users in the system
    ROLE_CHOICES = (
        ('ADMIN', 'Admin'),
        ('TEACHER', 'Teacher'),
        ('STUDENT', 'Student'),
    )

    # Role field to define user type (Admin, Teacher, Student)
    role = models.CharField(
        max_length=10,
        choices=ROLE_CHOICES
    )

    # String representation of user (shown in admin panel)
    def __str__(self):
        return self.username