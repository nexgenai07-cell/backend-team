from django.db import models
from users.models import Student
from products.models import Product
class Order(models.Model):
    """
    Order Model
    Stores customer order information.
    """

    # ForeignKey creates a One-to-Many relationship (A student can place multiple orders)
    # on_delete=models.CASCADE means if a Student is deleted, their orders will also be deleted automatically
    # related_name='orders' allows fetching a student's orders using 'student.orders.all()'
    customer = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        related_name='orders'
    )

    # ManyToManyField creates a relationship where an Order can have multiple Products, 
    # and a single Product can belong to multiple Orders. Django automatically creates a join table for this.
    # related_name='orders' allows fetching all orders for a specific product using 'product.orders.all()'
    products = models.ManyToManyField(
        Product,
        related_name='orders'
    )
    quantity = models.PositiveIntegerField(default=1)
    # Automatically sets the field to the current date and time when the order object is first created
    created_at = models.DateTimeField(auto_now_add=True)

    # Dunder (double underscore) string method to return a human-readable string representation of the object
    # Displays "Order #1", "Order #2", etc., in the Django Admin panel and shell
    def __str__(self):
        return f"Order #{self.id}"