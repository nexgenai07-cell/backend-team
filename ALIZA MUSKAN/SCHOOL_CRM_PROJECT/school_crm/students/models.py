from django.db import models
from classrooms.models import Classroom  # Importing Classroom model for ForeignKey relation

class Student(models.Model):
    """
    Student Model to store complete academic and personal details of a student.
    Tracks their assigned classroom and profile records.
    """
    full_name = models.CharField(max_length=255, help_text="Full name of the student.") 
    email = models.EmailField(unique=True, help_text="Unique personal or guardian email address.")  
    age = models.IntegerField(help_text="Age of the student.")  #
    roll_number = models.CharField(max_length=50, unique=True, help_text="Unique roll number assigned to the student.") 
    profile_image = models.ImageField(upload_to='students/', blank=True, null=True, help_text="Profile picture of the student.") 
    
    # Many students can belong to one classroom (Many-to-One relationship)
    classroom = models.ForeignKey(
        Classroom,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='students',  # Allows accessing students from a classroom instance (e.g., classroom.students.all())
        help_text="The classroom to which the student is assigned."
    )  

    def __str__(self):
        """Returns the string representation of the student."""
        return f"{self.full_name} ({self.roll_number})"