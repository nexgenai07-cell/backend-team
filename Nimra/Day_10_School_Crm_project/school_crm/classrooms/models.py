from django.db import models
from teachers.models import Teacher   # Teacher model import kiya, taake classroom ka teacher assign ho sake

class Classroom(models.Model):
    class_name = models.CharField(max_length=50)   # Class ka naam (e.g. "10th")
    section = models.CharField(max_length=10)      # Section ka naam (e.g. "A")
    room_number = models.CharField(max_length=10)  # Room number (e.g. "101")
    class_teacher = models.ForeignKey(
        Teacher,                                   # Har classroom ka ek teacher assign hoga
        on_delete=models.SET_NULL,                 # Agar teacher delete ho jaye to classroom delete na ho, sirf teacher null ho jaye
        null=True, blank=True                      # Teacher optional hai (classroom bina teacher ke bhi ho sakta hai)
    )

    def __str__(self):
        return f"{self.class_name} - {self.section}"  
        # Admin panel mein classroom ka naam aur section show hoga (e.g. "10th - A")
