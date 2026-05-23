from django.db import models

# Create your models here.
from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    age = models.IntegerField()
    class_name = models.CharField(max_length=10)
    roll_no = models.IntegerField(unique=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
class Teacher(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    age = models.IntegerField()
    subject = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
class Class(models.Model):
                    name = models.CharField(max_length=10)
                    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
                    students = models.ManyToManyField(Student)
                    
                    def __str__(self):
                     return self.name
from django.http import JsonResponse
def school_info(request):
       data = {
        "school_name": "Nimra Public School",
        "address": "Sahiwal, Pakistan",
        "contact": "+92-300-1234567",
        "principal": "Mr. Asad",
        "total_students": 500,
        "total_teachers": 25
    }
       return JsonResponse(data)
