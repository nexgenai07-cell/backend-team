# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):

    ROLE_CHOICES = (
        ('seller', 'Seller'),
    )

    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return self.username
    
