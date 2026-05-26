from django.db import models

# Student Model jiski humne API banani hai
class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    age = models.IntegerField()
    class_name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
# Teacher Model for Task 3
class Teacher(models.Model):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name
    
# Task 12 & 13: Class Model
class Class(models.Model):
    class_name = models.CharField(max_length=50)
    section = models.CharField(max_length=10)
    # ForeignKey ke zariye Teacher model se link kiya
    class_teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.class_name} - {self.section}"