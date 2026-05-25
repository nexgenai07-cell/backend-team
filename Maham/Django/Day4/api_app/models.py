from django.db import models

# Day 4: Student ka core model jahan database ka table design ho raha hai
class Student(models.Model):
    # Student ka naam store karne ke liye character field (max length 100)
    name = models.CharField(max_length=100)
    
    # Student ki email store karne ke liye email field (har student ki email unique honi chahiye)
    email = models.EmailField(unique=True)
    
    # Student ki age store karne ke liye integer (number) field
    age = models.IntegerField()
    
    # Student ki class ka naam store karne ke liye character field (jaise 10th, 11th)
    class_name = models.CharField(max_length=50)

    # Yeh function admin panel mein object ID ki jagah student ka real naam dikhane ke liye hai
    def __str__(self):
        return self.name
    
# =========================================================================
# TASK 9: TEACHER MODEL
# =========================================================================
class Teacher(models.Model):
    # Teacher ka naam aur unka subject fields
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name

# =========================================================================
# TASK 10: CLASSROOM MODEL
# =========================================================================
class Classroom(models.Model):
    # Classroom ki details jo task requirement ke mutabiq hain
    class_name = models.CharField(max_length=50)   # e.g., "10th"
    section = models.CharField(max_length=10)      # e.g., "A"
    total_students = models.IntegerField()         # e.g., 40
    class_teacher = models.CharField(max_length=100) # e.g., "Ahmed"

    def __str__(self):
        return f"{self.class_name} - Section {self.section}"
    
# =========================================================================
# TASK 11: STUDENT ATTENDANCE MODEL
# =========================================================================
class Attendance(models.Model):
    # Student ka naam (Task requirement ke mutabiq char field rakha hai)
    student = models.CharField(max_length=100) # e.g., "Ali"
    
    # Date store karne ke liye DateField
    date = models.DateField()                  # e.g., "2026-05-13"
    
    # Status store karne ke liye text field (Present/Absent)
    status = models.CharField(max_length=20)   # e.g., "Present"

    def __str__(self):
        return f"{self.student} - {self.date} ({self.status})"

# =========================================================================
# TASK 12: STUDENT RESULT MODEL
# =========================================================================
class Result(models.Model):
    # Student aur Subject details jo task input mein hain
    student = models.CharField(max_length=100) # e.g., "Ali"
    subject = models.CharField(max_length=100) # e.g., "Math"
    
    # Marks ke liye Integer field aur Grade ke liye Char field
    marks = models.IntegerField()              # e.g., 90
    grade = models.CharField(max_length=10)   # e.g., "A"

    def __str__(self):
        return f"{self.student} - {self.subject}: {self.marks} ({self.grade})"
    
# =========================================================================
# TASK 13: E-COMMERCE PRODUCT MODEL
# =========================================================================
class Product(models.Model):
    # Product ki saari basic details jo task requirement mein hain
    name = models.CharField(max_length=200)             # e.g., "Laptop"
    price = models.DecimalField(max_digits=10, decimal_places=2) # e.g., 100000.00
    stock = models.IntegerField()                       # e.g., 10
    description = models.TextField()                    # e.g., "Gaming laptop"
    category = models.CharField(max_length=100)         # e.g., "Electronics"

    def __str__(self):
        return self.name

# =========================================================================
# TASK 16: CART MODEL
# =========================================================================
class Cart(models.Model):
    # Kis user ka cart hai aur us mein konsa product kitni quantity mein hai
    user = models.CharField(max_length=100)            # e.g., "Ali"
    product = models.CharField(max_length=200)         # e.g., "Laptop"
    quantity = models.IntegerField(default=1)          # e.g., 1

    def __str__(self):
        return f"{self.user}'s Cart - {self.product} ({self.quantity})"

# =========================================================================
# TASK 17: ORDER MODEL
# =========================================================================
class Order(models.Model):
    user = models.CharField(max_length=100)            # e.g., "Ali"
    
    # JSONField use kar rahe hain taake aik order mein multiple products ki list store ho sake
    products = models.JSONField()                      # e.g., ["Laptop", "Mouse"]
    total_amount = models.DecimalField(max_digits=10, decimal_places=2) # e.g., 100000.00
    order_status = models.CharField(max_length=50, default="Pending")  # e.g., "Pending"

    def __str__(self):
        return f"Order {self.id} by {self.user} - {self.order_status}"