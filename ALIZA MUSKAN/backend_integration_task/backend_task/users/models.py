from django.db import models
# name → user ka naam
# email → unique email
# profile_image → image upload
# __str__ → admin mein naam show karega
class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    profile_image = models.ImageField(
        upload_to='profile_images/',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name
    
# Stores Gemini AI requests and responses
class AIRequest(models.Model):

    # User prompt sent to Gemini
    prompt = models.TextField()

    # Gemini generated response
    response = models.TextField(
        blank=True,
        null=True
    )

    # Record creation timestamp
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    def __str__(self):
        return self.prompt[:50]
class Payment(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('successful', 'Successful'),
        ('failed', 'Failed'),
    ]

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    stripe_payment_id = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Payment {self.id} - {self.amount}"