from django.db import models
from classrooms.models import Classroom   # Classroom model ko import kiya, taake Student usse link ho sake

class Student(models.Model):
    full_name = models.CharField(max_length=100)  
    # Student ka naam store karega, max 100 characters tak

    email = models.EmailField(unique=True)  
    # Email field, unique rakha hai taake duplicate email na ho

    age = models.IntegerField()  
    # Student ki age store karega, integer format mein

    roll_number = models.CharField(max_length=20, unique=True)  
    # Roll number har student ka unique hoga, max 20 characters

    profile_image = models.ImageField(upload_to='students/', null=True, blank=True)

    # Student ki profile image upload hogi, 'media/students/' folder mein save hogi

    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)  
    # Har student ek classroom se linked hoga, agar classroom delete ho to uske students bhi delete ho jaayenge

    def __str__(self):
        return self.full_name  
    # Admin panel mein student ka naam show hoga
