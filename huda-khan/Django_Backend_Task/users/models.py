from django.db import models
from cloudinary.models import CloudinaryField


class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    profile_image = CloudinaryField('image')

    def __str__(self):
        return self.name