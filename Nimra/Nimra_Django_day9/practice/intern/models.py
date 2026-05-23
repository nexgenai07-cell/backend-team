from django.db import models   # Import Django's built-in ORM tools

# ✅ Student model = database table for storing student records
class Student(models.Model):
    name = models.CharField(max_length=100)       # Student ka naam
    age = models.IntegerField(default=18)   # ✅ default value set                # Student ki age
    email = models.EmailField()                   # Student ka email
    profile_pic = models.ImageField(upload_to='students/', null=True, blank=True)  
    # profile picture field (MEDIA_ROOT/students/ folder me save hoga)

    # ✅ ForeignKey to Classroom (optional link)
    classroom = models.ForeignKey('Classroom', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name


# ✅ Teacher model = database table for storing teacher records
class Teacher(models.Model):
    name = models.CharField(max_length=100)       # Teacher ka naam
    subject = models.CharField(max_length=100)    # Subject jo teacher padhata hai
    email = models.EmailField(unique=True)        # Unique email address

    def __str__(self):
        return self.name


# ✅ Classroom model = har class ka record
class Classroom(models.Model):
    name = models.CharField(max_length=100)       # Class ka naam (e.g. "10th-A")
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)  
    # har classroom ka ek teacher hoga

    def __str__(self):
        return self.name


# ✅ Product model = e-commerce products
class Product(models.Model):
    name = models.CharField(max_length=100)       # Product ka naam
    price = models.IntegerField()                 # Price (integer for simplicity)
    stock = models.IntegerField()                 # Available quantity
    category = models.CharField(max_length=100)   # Category (Electronics, Clothing, etc.)
    description = models.TextField(blank=True)    # Optional description
    thumbnail = models.ImageField(upload_to='products/thumbnails/', null=True, blank=True)
    image = models.ImageField(upload_to='products/images/', null=True, blank=True)

    def __str__(self):
        return self.name


# ✅ Order model = students ke orders
class Order(models.Model):
    customer = models.ForeignKey(Student, on_delete=models.CASCADE)   # ek student order karega
    products = models.ManyToManyField(Product)                        # multiple products ek order me
    created_at = models.DateTimeField(auto_now_add=True)              # order date/time

    def __str__(self):
        return f"Order {self.id} by {self.customer.name}"
