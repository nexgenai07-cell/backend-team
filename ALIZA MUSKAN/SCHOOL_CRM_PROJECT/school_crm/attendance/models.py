from django.db import models
from students.models import Student  # Importing Student model for ForeignKey relation

class Attendance(models.Model):
    """
    Attendance Model to track daily attendance records of students.
    """
    # Attendance statuses using TextChoices
    class StatusChoices(models.TextChoices):
        PRESENT = 'PRESENT', 'Present'
        ABSENT = 'ABSENT', 'Absent'
        LATE = 'LATE', 'Late'

    # Foreign Key linking to the Student model
    # related_name='attendance_records' allows us to fetch attendance from a student instance easily
    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        related_name='attendance_records',
        help_text="The student whose attendance is being recorded."
    )
    date = models.DateField(help_text="The date of the attendance record.")
    status = models.CharField(
        max_length=10,
        choices=StatusChoices.choices,
        default=StatusChoices.PRESENT,
        help_text="The status of attendance (Present, Absent, Late)."
    )

    class Meta:
        # Enforces that a student can only have one attendance record per day
        unique_together = ('student', 'date')

    def __str__(self):
        """Returns string representation showing student name, date and status."""
        return f"{self.student.full_name} - {self.date} ({self.status})"