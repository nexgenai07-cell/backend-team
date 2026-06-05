from django.db import models

# ========================================================
# CLASSROOM MODEL (Classroom ki basic details store krne k liye)
# ========================================================
class Classroom(models.Model):
    name = models.CharField(max_length=50, unique=True) # Class ka naam (e.g., Class 10-A)
    section = models.CharField(max_length=10)           # Section (e.g., A, B, C)

    def __str__(self):
        return f"{self.name} ({self.section})"