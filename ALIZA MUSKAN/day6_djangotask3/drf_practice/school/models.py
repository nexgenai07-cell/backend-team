from django.db import models
# from school.models import Student,Teacher

class Student(models.Model):

    name = models.CharField(max_length=100)

    age = models.IntegerField()

    def __str__(self):

        return self.name
    
class Teacher(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    
class Class(models.Model):
    name = models.CharField(max_length=50)
    section = models.CharField(max_length=10)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
    