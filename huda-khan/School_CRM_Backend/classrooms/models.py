from django.db import models

# Classroom model
class Classroom(models.Model):

    # Name of class (e.g., Grade 10)
    class_name = models.CharField(max_length=100)

    # Section (A, B, C)
    section = models.CharField(max_length=10)

    # Room number
    room_number = models.IntegerField()

    # Class teacher (will connect later)
    class_teacher = models.ForeignKey(
        'teachers.Teacher',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    def __str__(self):
        return f"{self.class_name} - {self.section}"