# Import serializers from Django REST Framework
from rest_framework import serializers

# Import custom user model
from .models import User
from django.contrib.auth.password_validation import validate_password



# Serializer for Register API
class RegisterSerializer(serializers.ModelSerializer):

    # Password field (write_only = won't show in response)
    password = serializers.CharField(write_only=True, validators=[validate_password])
    email = serializers.EmailField(required=True)
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'role']

    # Custom create method to handle user creation
    def create(self, validated_data):

        # Use create_user (important for password hashing)
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            role=validated_data['role']
        )

        return user