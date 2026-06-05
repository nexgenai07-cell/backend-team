# Importing the serializers module from Django Framework to handle data validation and serialization
from rest_framework import serializers

# Importing get_user_model to dynamically fetch the active User model defined in settings.AUTH_USER_MODEL
from django.contrib.auth import get_user_model

# Fetch the active CustomUser model configured in settings.py (Good practice for flexibility)
User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    """
    Serializer to handle user registration.
    Validates input and creates a new user with an encrypted password.
    """
    # Write-only password field to ensure it is never exposed in responses.
    # style={'input_type': 'password'} renders it as a password field in the browsable API.
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})
    
    # FIX: Overriding role as a plain CharField so DRF's strict choice validation 
    # doesn't block lowercase inputs (like 'teacher') before validation methods can run.
    role = serializers.CharField(required=False, default='STUDENT')

    class Meta:
        # Linking this serializer to the active User model
        model = User
        # Defining the specific fields that this serializer will accept during registration
        fields = ['username', 'email', 'password', 'role', 'phone_number', 'profile_picture']

    def validate_email(self, value):
        """
        Validates that the email is unique across the application.
        """
        # Checking database if any user already exists with the provided email value
        if User.objects.filter(email=value).exists():
            # Raising a validation error if the email is already taken
            raise serializers.ValidationError("A user with this email already exists.")
        # Returning the validated email value if it is unique
        return value

    def validate_role(self, value):
        """
        UX FIX: Automatically converts the input role string to UPPERCASE.
        Accepts lowercase input ('teacher') and normalizes it to database standards ('TEACHER').
        """
        if value:
            upper_value = value.upper()
            # Dynamically fetching valid choices from the User Model's RoleChoices
            # (Adjusted to RoleChoices based on standard model structure)
            valid_roles = [choice[0] for choice in User.Roles.choices]
            if upper_value not in valid_roles:
                raise serializers.ValidationError(f"'{value}' is not a valid role. Choose from Admin, Teacher, or Student.")
            return upper_value
        return 'STUDENT'

    def create(self, validated_data):
        """
        Overriding the create method to ensure the user password 
        is hashed using Django's set_password mechanism.
        """
        # Using create_user instead of create to automatically handle password hashing/encryption safely
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email', ''), # .get() handles optional fields safely to avoid KeyError
            password=validated_data['password'],
            role=validated_data.get('role', 'STUDENT'), # Uses cleaned uppercase role from validation
            phone_number=validated_data.get('phone_number', ''),
            profile_picture=validated_data.get('profile_picture', None)
        )
        # Returning the newly created user instance back to the view
        return user


class UserProfileSerializer(serializers.ModelSerializer):
    """
    Serializer to display and update the authenticated user's profile details.
    """
    # Role is read-only to prevent users from escalating their own privileges (e.g., changing from Student to Admin)
    role = serializers.CharField(read_only=True)

    class Meta:
        # Linking this serializer to the active User model for profile management
        model = User
        # Fields to expose when viewing or updating the user profile (includes read-only 'id' and 'date_joined')
        fields = ['id', 'username', 'email', 'role', 'phone_number', 'profile_picture', 'date_joined']