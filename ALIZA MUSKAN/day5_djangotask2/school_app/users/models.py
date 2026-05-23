from django.db import models

# Create your models here.
from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    age = models.IntegerField()
    class_name = models.CharField(max_length=50)
    roll_no = models.IntegerField(unique=True)
    is_active = models.BooleanField(default=True)
    def __str__(self):
        return self.name
class Teacher(models.Model):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    joining_date = models.DateField()

    def __str__(self):
        return self.name
class SchoolClass(models.Model):
    class_name = models.CharField(max_length=50)
    section = models.CharField(max_length=10)
    total_students = models.IntegerField()

    class_teacher = models.ForeignKey(
        Teacher,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.class_name} - {self.section}"