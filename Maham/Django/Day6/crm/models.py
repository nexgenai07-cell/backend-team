from django.db import models

class Classroom(models.Model):
    """
    Classroom Model: Student kis class ya section mei hai, us ki details save karega.
    """
    name = models.CharField(max_length=50)       # Class ka naam (e.g., BSIT, CS)
    section = models.CharField(max_length=10)    # Section (e.g., Morning, Evening)

    def __str__(self):
        return f"{self.name} - {self.section}"


class Teacher(models.Model):
    """
    Teacher Model (Task 2): Is model ke ooper CRUD operations chalenge.
    """
    name = models.CharField(max_length=100)      # Teacher ka naam
    email = models.EmailField(unique=True)       # Teacher ki unique email id
    subject = models.CharField(max_length=100)   # Jo subject wo parhate hain

    def __str__(self):
        return self.name


class Student(models.Model):
    """
    Student Model (Task 1 & Task 10): Is mei classroom ka Foreign Key relation hai,
    aur profile image upload karne ka option hai.
    """
    # ForeignKey: Aik classroom mei bohat se students ho sakte hain (One-to-Many relation)
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE, related_name='students')
    name = models.CharField(max_length=100)
    roll_number = models.CharField(max_length=20, unique=True)
    
    # Task 10: Profile Image Upload. Image 'media/student_profiles/' folder mei save hogi
    profile_image = models.ImageField(upload_to='student_profiles/', null=True, blank=True)

    def __str__(self):
        return self.name