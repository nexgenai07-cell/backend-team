from django.db import models

# ✅ Teacher model banaya ja raha hai jo teacher ka data store karega
class Teacher(models.Model):
    full_name = models.CharField(max_length=100)   
    # Teacher ka naam (max 100 characters)

    email = models.EmailField(unique=True)         
    # Teacher ka email, unique rakha hai taake duplicate na ho

    subject = models.CharField(max_length=50)      
    # Subject jo teacher padhata hai (e.g. "Maths", "Science")

    salary = models.DecimalField(max_digits=10, decimal_places=2)  
    # Salary ko decimal format mein store kiya (accurate financial data ke liye)

    profile_image = models.ImageField(upload_to='teachers/')       
    # Teacher ki profile image upload hogi 'media/teachers/' folder mein

    def __str__(self):
        return self.full_name   
        # Admin panel mein teacher ka naam show hoga instead of "Teacher object"
