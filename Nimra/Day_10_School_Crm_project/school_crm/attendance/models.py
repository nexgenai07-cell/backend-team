from django.db import models
from students.models import Student   # Student model import kiya taake attendance uske sath link ho

class Attendance(models.Model):
    # ✅ Status choices define kiye (sirf 3 options allowed honge)
    STATUS_CHOICES = [
        ('Present', 'Present'),
        ('Absent', 'Absent'),
        ('Leave', 'Leave'),
    ]

    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    # Har attendance ek student ke sath linked hoga
    # Agar student delete ho jaye to uska attendance bhi delete ho jaayega (CASCADE)

    date = models.DateField()
    # Attendance ka din store karega

    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    # Attendance ka status (Present/Absent/Leave) sirf defined choices mein se hoga

    class Meta:
        unique_together = ('student', 'date')
        # ✅ Ek student ke liye ek din par sirf ek attendance record allowed hoga
        # Duplicate entry prevent karne ke liye

    def __str__(self):
        return f"{self.student.full_name} - {self.date} - {self.status}"
        # Admin panel mein readable output: "Ali - 2026-05-22 - Present"
