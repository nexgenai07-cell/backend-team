from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('teacher', 'Teacher'),
        ('student', 'Student'),
        ('customer', 'Customer'),
        ('seller', 'Seller'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='customer')
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.username} ({self.role})"

# Task 13: Product Model (Sellers can create, Customers can view)
class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    seller = models.ForeignKey(CustomUser, on_delete=models.CASCADE, limit_choices_to={'role': 'seller'})

    def __str__(self):
        return self.name

# Task 14: Cart System
class CartItem(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, limit_choices_to={'role': 'customer'})
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

# Task 15: Order System
class Order(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    created_at = models.DateTimeField(auto_now_add=True)