from django.db import models

class UserProfile(models.Model):
    """
    1. User Model: Field for Name, Email, and Profile Image.
    Images uploaded will automatically route to Cloudinary via storage configuration.
    """
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    profile_image = models.ImageField(upload_to='profile_images/')

    def __str__(self):
        return self.name


class AIRequest(models.Model):
    """
    4. Gemini API Integration Model: Stores Prompt, Response, and Timestamp.
    """
    prompt = models.TextField()
    response = models.TextField(blank=True, null=True)  # blank=True taake shuru mei empty save ho sake
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Prompt: {self.prompt[:30]}..."


class Payment(models.Model):
    """
    5. Stripe Integration Model: Connects with User, tracks Amount, Intent ID, and Status.
    """
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('SUCCESS', 'Success'),
        ('FAILED', 'Failed'),
    ]

    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='payments')
    amount = models.DecimalField(max_digits=10, decimal_places=2)  # For currency amounts
    stripe_payment_id = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Payment of {self.amount} by {self.user.name} - {self.status}"