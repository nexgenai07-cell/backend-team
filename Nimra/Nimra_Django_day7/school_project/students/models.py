from django.db import models   # Django ka models module import karte hain

# -------------------------------
# ✅ Student Model
# -------------------------------
class Student(models.Model):
    name = models.CharField(max_length=100)       # Student ka naam (text field, max 100 chars)
    email = models.EmailField()                   # Student ka email (valid email format)
    age = models.IntegerField()                   # Student ki age (integer value)
    class_name = models.CharField(max_length=20)  # Student ki class (e.g., "10th A")
    roll_no = models.IntegerField()               # Roll number (unique identifier for student)
    is_active = models.BooleanField(default=True) # Active status (True/False)

    def __str__(self):
        return self.name   # Admin panel me student ka naam show hoga instead of "Student object"


# -------------------------------
# ✅ Teacher Model
# -------------------------------
class Teacher(models.Model):
    name = models.CharField(max_length=100)       # Teacher ka naam
    subject = models.CharField(max_length=50)     # Subject jo teacher padhata hai
    email = models.EmailField(unique=True)        # Teacher ka email (unique hona chahiye)
    salary = models.IntegerField()                # Teacher ki salary
    joining_date = models.DateField()             # Teacher ki joining date

    def __str__(self):
        return self.name   # Admin panel me teacher ka naam show hoga


# -------------------------------
# ✅ Classroom Model
# -------------------------------
class Classroom(models.Model):
    class_name = models.CharField(max_length=20)  # Class ka naam (e.g., "10th")
    section = models.CharField(max_length=5)      # Section (e.g., "A")
    total_students = models.IntegerField()        # Total students count in class
    class_teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)  
    # ForeignKey → har class ka ek teacher assign hoga
    # on_delete=models.CASCADE → agar teacher delete ho jaye to uski class bhi delete ho jayegi

    def __str__(self):
        return f"{self.class_name} - {self.section}"   # Admin panel me class ka naam aur section show hoga
class Attendance(models.Model):
    student = models.CharField(max_length=100)     # Student ka naam
    date = models.DateField()                      # Attendance date
    status = models.CharField(max_length=10)       # "Present" / "Absent"

    def __str__(self):
        return f"{self.student} - {self.date} - {self.status}"
class Result(models.Model):
    student = models.CharField(max_length=100)     # Student ka naam
    subject = models.CharField(max_length=50)      # Subject ka naam
    marks = models.IntegerField()                  # Marks (integer)
    grade = models.CharField(max_length=2)         # Grade (e.g., A, B, C)

    def __str__(self):
        return f"{self.student} - {self.subject} - {self.grade}"
class Product(models.Model):
    name = models.CharField(max_length=100)          # Product ka naam
    price = models.IntegerField()                    # Product ki price
    stock = models.IntegerField()                    # Available stock
    description = models.TextField()                 # Product description
    category = models.CharField(max_length=50)       # Product category

    def __str__(self):
        return f"{self.name} - {self.category}"
class Cart(models.Model):
    user = models.CharField(max_length=100)                # User ka naam
    product = models.CharField(max_length=100)             # Product ka naam
    quantity = models.IntegerField(default=1)              # Quantity of product

    def __str__(self):
        return f"{self.user} - {self.product} ({self.quantity})"
class Order(models.Model):
    user = models.CharField(max_length=100)
    product = models.CharField(max_length=100)
    quantity = models.IntegerField()
    total_price = models.IntegerField()
    order_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Order by {self.user} - {self.product}"

