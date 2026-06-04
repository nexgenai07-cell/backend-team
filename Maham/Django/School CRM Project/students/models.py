from django.db import models
from django.conf import settings
from classrooms.models import Classroom

# ========================================================
# STUDENT MODEL (Students ki details store krne k liye)
# ========================================================
class Student(models.Model):
    # Har student ka link accounts.User model ke sath hoga (Jahan role='STUDENT' ho)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='student_profile')
    
    # Classroom ke sath ForeignKey relation (Aik class mei bht se students ho sakte hain)
    classroom = models.ForeignKey(Classroom, on_delete=models.SET_NULL, null=True, blank=True, related_name='students')
    
    age = models.IntegerField()
    roll_number = models.CharField(max_length=20, unique=True)
    
    # Student ki profile image (media/students/ folder mei save hogi)
    profile_image = models.ImageField(upload_to='students/', null=True, blank=True)

    def __str__(self):
        return f"Student: {self.user.username} - Roll No: {self.roll_number}"