from django.db import models
from django.conf import settings
from students.models import Student

# ========================================================
# ATTENDANCE MODEL (Students ki daily attendance record krne k liye)
# ========================================================
class Attendance(models.Model):
    STATUS_CHOICES = (
        ('PRESENT', 'Present'),
        ('ABSENT', 'Absent'),
    )

    # Student ke sath ForeignKey relation (Aik student ki bht si dates ki attendance ho sakti hai)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='attendance_records')
    date = models.DateField() # Kis din ki attendance hai
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)

    class Meta:
        # ⚠️ PDF Requirement: Aik student ki aik date par double entry na ho sake
        unique_together = ('student', 'date')

    def __str__(self):
        return f"{self.student.user.username} - {self.date} - {self.status}"