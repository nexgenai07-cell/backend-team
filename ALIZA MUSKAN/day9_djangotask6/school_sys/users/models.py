from django.db import models
class Student(models.Model):
    # Student model stores student information.
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    age = models.PositiveIntegerField()
 # Profile Image
    profile_image = models.ImageField( upload_to='student_images/', null=True, blank=True)
    classroom = models.ForeignKey(
        'Classroom',
        on_delete=models.CASCADE,
        related_name='students',
        null=True,
        blank=True
    )
    def __str__(self):
        # Display student name in admin panel.
        return self.name
    

# task2
class Teacher(models.Model):
    """
    Teacher Model
    Stores teacher data for API system
    """
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    experience = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name
class Classroom(models.Model):
    """
    Classroom Model
        Stores information about individual school classrooms and establishes 
    a relationship to assign a specific teacher to each classroom.
    """
    # Unique or descriptive name for the classroom (e.g., "Grade 10-A", "Bio Lab")
    name = models.CharField(
        max_length=100,
        help_text="Enter the name or designation of the classroom."
    )
    # Many-to-One relationship with the Teacher model.
    # - on_delete=models.CASCADE: If a teacher profile is deleted, all associated 
    #   classrooms will also be deleted automatically.
    # - related_name='classrooms': Enables reverse lookup, allowing you to access 
    #   a teacher's assigned classes using `teacher.classrooms.all()`.
    teacher = models.ForeignKey(
        Teacher,
        on_delete=models.CASCADE,
        related_name='classrooms',
        help_text="Select the teacher assigned to this classroom."
    )

    def __str__(self):
        """
        Returns the string representation of the Classroom instance.
        Displays the classroom name in the Django Admin panel and shell.
        """
        return self.name