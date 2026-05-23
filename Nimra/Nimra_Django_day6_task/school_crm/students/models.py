from django.db import models   # Django ke ORM models import

# Student model banaya jo database table represent karega
class Student(models.Model):
    name = models.CharField(max_length=100)                  # Student ka naam
    email = models.EmailField(unique=True)                   # Email (unique hona chahiye)
    age = models.IntegerField()                              # Age
    class_name = models.CharField(max_length=50, blank=True, null=True)  # Class optional
    roll_no = models.IntegerField(blank=True, null=True)     # Roll number optional
    is_active = models.BooleanField(default=True)            # Active status (default True)

    def __str__(self):
        return self.name   # Admin panel me student ka naam show hoga


# Teacher model banaya
class Teacher(models.Model):
    name = models.CharField(max_length=100)          # Teacher ka naam
    subject = models.CharField(max_length=100)       # Subject jo teacher padhata hai
    email = models.EmailField(unique=True)           # Email (unique hona chahiye)
    salary = models.IntegerField(default=30000)      # Salary (default 30000)
    joining_date = models.DateField()                # Joining date

    def __str__(self):
        return self.name   # Admin panel me teacher ka naam show hoga

# Class Model → school classes ki info store karega
class Class(models.Model):
    name = models.CharField(max_length=50)           # Class ka naam (e.g. 10th)
    section = models.CharField(max_length=10)        # Section (e.g. A, B)
    strength = models.IntegerField()                 # Students ki strength

    def __str__(self):
        return f"{self.name} - {self.section}"       # Admin panel me class + section show hoga