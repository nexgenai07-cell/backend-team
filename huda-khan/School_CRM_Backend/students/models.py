from django.db import models
from classrooms.models import Classroom

class Student(models.Model):
    name = models.CharField(max_length=100)
    roll_number = models.CharField(max_length=20)

    classroom = models.ForeignKey(
        Classroom,
        on_delete=models.CASCADE,
        related_name='students'
    )

    image = models.ImageField(
        upload_to='students/',
        blank=True,
        null=True
    )

    def __str__(self):
        return f"{self.name} ({self.roll_number})"