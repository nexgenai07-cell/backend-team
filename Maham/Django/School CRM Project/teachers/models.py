from django.db import models
from django.conf import settings

# ========================================================
# TEACHER MODEL (Teachers ki profile details store krne k liye)
# ========================================================
class Teacher(models.Model):
    # Har teacher ka link accounts.User model ke sath hoga (Jahan role='TEACHER' ho)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='teacher_profile')
    
    subject = models.CharField(max_length=100) # Teacher kaun sa subject parhate hain
    phone = models.CharField(max_length=15)    # Contact number
    
    # Profile image upload karne ke liye (media/teachers/ folder mei save hogi)
    profile_image = models.ImageField(upload_to='teachers/', null=True, blank=True)

    def __str__(self):
        return f"Teacher: {self.user.username} - {self.subject}"