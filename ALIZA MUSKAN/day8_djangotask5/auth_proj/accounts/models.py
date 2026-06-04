from django.db import models
from django.contrib.auth.models import AbstractUser

class Student(AbstractUser):

    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('student', 'Student'),
        ('teacher', 'Teacher'),
    )

    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return self.username