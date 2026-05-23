from django.db import models

# Teacher model
class Teacher(models.Model):

    # Teacher full name
    full_name = models.CharField(max_length=100)

    # Email
    email = models.EmailField(unique=True)

    # Subject they teach
    subject = models.CharField(max_length=100)

    # Salary
    salary = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.full_name
    
    
    
    
    
    # class_teacher = models.ForeignKey(
#     'teachers.Teacher',
#     on_delete=models.SET_NULL,
#     null=True,
#     blank=True
# )