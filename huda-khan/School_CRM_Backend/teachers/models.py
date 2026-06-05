from django.db import models

class Teacher(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    subject = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=10, decimal_places=2)

    image = models.ImageField(
        upload_to='teachers/',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.full_name