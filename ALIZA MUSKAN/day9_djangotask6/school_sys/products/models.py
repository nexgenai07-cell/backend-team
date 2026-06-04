from django.db import models

# Create your models here.
class Product(models.Model):
    """
    Product Model
    Stores product information.
    This model will be used in the e-commerce APIs.
    """
    # Product name
    name = models.CharField(max_length=200)
    # Product price
    price = models.DecimalField(max_digits=10, decimal_places=2)
    # Available stock quantity
    stock = models.PositiveIntegerField()
    # Product category
    category = models.CharField( max_length=100)
    # Product details
    description = models.TextField()
    # Creation timestamp
    created_at = models.DateTimeField( auto_now_add=True)

#  Image fields
    thumbnail = models.ImageField(upload_to='product_thumbnails/',null=True,blank=True)

    image = models.ImageField( upload_to='product_images/', null=True, blank=True)
    
    def __str__(self):
        """
        Display product name in admin panel.
        """
        return self.name