from django.db import models

class Product(models.Model):
    """
    Product Model (Task 3 & Task 11): Is mei product ke details aur images upload karne ke fields hain.
    """
    name = models.CharField(max_length=200)                         # Product ka naam (e.g., iPhone)
    price = models.DecimalField(max_digits=10, decimal_places=2)    # Product ki keemat
    stock = models.IntegerField()                                   # Kitne products available hain inventory mei
    category = models.CharField(max_length=100)                     # Category (e.g., electronics, clothing)
    description = models.TextField()                                # Product ki detail description
    
    # Task 11: Seller product thumbnail aur main image upload kar sake
    thumbnail = models.ImageField(upload_to='products/thumbnails/', null=True, blank=True)
    product_image = models.ImageField(upload_to='products/images/', null=True, blank=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    """
    Order Model (Task 14): Jo nested serializer seekhne ke liye zaroori hai.
    Aik order mei multiple products ho sakte hain (Many-to-Many Relation).
    """
    customer_name = models.CharField(max_length=100)   # Order karne wale customer ka naam
    customer_email = models.EmailField()              # Customer ki email address
    
    # ManyToManyField: Aik product multiple orders mei ho sakta hai, aur aik order mei multiple products ho sakte hain
    products = models.ManyToManyField(Product, related_name='orders')
    created_at = models.DateTimeField(auto_now_add=True)  # Jis time order create hua

    def __str__(self):
        return f"Order #{self.id} by {self.customer_name}"