from django.db import models
from teachers.models import Teacher # Importing Teacher for ForeignKey relationship

class Classroom(models.Model):
    """
    Classroom Model representing academic classes linked with a class teacher.
    """
    class_name = models.CharField(max_length=50, help_text="Name of the class (e.g., Grade 10).")
    section = models.CharField(max_length=10, help_text="Section identifier (e.g., Section A).") 
    room_number = models.CharField(max_length=20, help_text="Physical room number in the school.") 
    
    # One teacher can be a class teacher of a classroom (One-to-Many / Foreign Key)
    class_teacher = models.ForeignKey(
        Teacher, 
        related_name='classrooms', # Accessible via teacher.classrooms.all()
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True,
        help_text="Assigned class teacher for this classroom."
    ) 

    def __str__(self):
        """Returns the complete classroom name with section."""
        return f"{self.class_name} - {self.section}"