from django.db import models

# Task 1: Student Model
class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    age = models.IntegerField()
    class_name = models.CharField(max_length=50)
    roll_no = models.CharField(max_length=20, unique=True)
    is_active = models.BooleanField(default=True)

    # Task 9: Student ka naam dikhane ke liye
    def __str__(self):
        return self.name


# Task 2: Teacher Model
class Teacher(models.Model):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    joining_date = models.DateField()

    # Task 9: Teacher ka naam dikhane ke liye
    def __str__(self):
        return self.name
    
# Task 8: Create Class Model
class Class(models.Model):
    class_name = models.CharField(max_length=50)
    section = models.CharField(max_length=10)
    total_students = models.IntegerField()
    
    # ForeignKey linking to Teacher model
    class_teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    # Task 9: String representation (Readable names)
    def __str__(self):
        return f"{self.class_name} - Section {self.section}"