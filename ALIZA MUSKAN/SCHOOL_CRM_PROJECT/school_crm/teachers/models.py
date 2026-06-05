from django.db import models

class Teacher(models.Model):
    """
    Teacher Model to store professional and personal details of faculty members.
    """
    full_name = models.CharField(max_length=255, help_text="Full name of the teacher.") 
    email = models.EmailField(unique=True, help_text="Unique professional email address.") 
    subject = models.CharField(max_length=100, help_text="Primary subject taught by the teacher.") 
    salary = models.DecimalField(max_digits=10, decimal_places=2, help_text="Monthly salary of the teacher.") 
    profile_image = models.ImageField(upload_to='teachers/', blank=True, null=True, help_text="Profile photo.") 

    def __str__(self):
        """Returns the string representation of the teacher."""
        return self.full_name