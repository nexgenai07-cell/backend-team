from django.contrib.auth.models import AbstractUser
from django.db import models
# for multi lang support
from django.utils.translation import gettext_lazy as _

class CustomUser(AbstractUser):
    """
    Custom User Model for the School CRM.
    Enforces Role-Based Access Control (RBAC) using choice fields.
    """
    
    # Define User Roles as Choices according to industry standards
    class Roles(models.TextChoices):
        ADMIN = 'ADMIN', _('Admin')
        TEACHER = 'TEACHER', _('Teacher')
        STUDENT = 'STUDENT', _('Student')

    # Role field to determine user permissions across the CRM
    role = models.CharField(
        max_length=10,
        choices=Roles.choices,
        default=Roles.STUDENT,
        help_text=_("Designates the role of the user within the School CRM.")
    )
    
    # Additional common profile fields
    phone_number = models.CharField(
        max_length=15, 
        blank=True, 
        null=True,
        help_text=_("Contact phone number of the user.")
    )
    profile_picture = models.ImageField(
        upload_to='profiles/', 
        blank=True, 
        null=True,
        help_text=_("Profile picture for the user account.")
    )

    def __str__(self):
        """Returns the string representation of the user."""
        return f"{self.username} ({self.get_role_display()})"

    # Helper methods to easily check roles in views and permissions
    @property
    def is_admin(self):
        """
        Property method to quickly check if the user has an Admin role.
        Returns True if the role is ADMIN, otherwise False.
        """
        return self.role == self.Roles.ADMIN

    @property
    def is_teacher(self):
        """
        Property method to quickly check if the user has a Teacher role.
        Returns True if the role is TEACHER, otherwise False.
        """
        return self.role == self.Roles.TEACHER

    @property
    def is_student(self):
        """
        Property method to quickly check if the user has a Student role.
        Returns True if the role is STUDENT, otherwise False.
        """
        return self.role == self.Roles.STUDENT
    def save(self, *args, **kwargs):
        """
        GLOBAL FIX: Automatically converts the incoming role string to UPPERCASE 
        before saving into the database. Works across APIs, Admin panel, and scripts.
        """
        if self.role and isinstance(self.role, str):
            # .upper() lagane se hamesha capital word hi database me save hoga
            self.role = self.role.upper()
        super().save(*args, **kwargs)