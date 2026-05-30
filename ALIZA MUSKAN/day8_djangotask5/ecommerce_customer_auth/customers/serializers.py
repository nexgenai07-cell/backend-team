# Import DRF serializer system
from rest_framework import serializers
# Import Django password validator
from django.contrib.auth.password_validation import validate_password

# Import custom Customer model
from .models import Customer

# Customer Registration Serializer

class CustomerRegistrationSerializer(serializers.ModelSerializer):

    # Password field
    # write_only=True means password response me show nahi hoga
    password = serializers.CharField(
        write_only=True,
        validators=[validate_password]
    )

    # Confirm password field
    password_confirm = serializers.CharField(
        write_only=True
    )

    class Meta:

        # Model define
        model = Customer

        # Fields jo API accept karegi
        fields = [
            'username',
            'email',
            'password',
            'password_confirm',
            'phone_number',
        ]

    # Object level validation
    def validate(self, attrs):

        # Check password match
        if attrs['password'] != attrs['password_confirm']:

            raise serializers.ValidationError({
                'password': 'Passwords do not match'
            })

        return attrs

    # Create new customer
    def create(self, validated_data):

        # Remove confirm password
        validated_data.pop('password_confirm')

        # create_user automatically hashes password
        user = Customer.objects.create_user(

            username=validated_data['username'],

            email=validated_data['email'],

            password=validated_data['password'],

            phone_number=validated_data['phone_number'],
        )

        return user

# Customer Login Serializer

class CustomerLoginSerializer(serializers.Serializer):

    # Username input
    username = serializers.CharField()

    # Password input
    password = serializers.CharField(
        write_only=True
    )

# Customer Profile Serializer
class CustomerProfileSerializer(serializers.ModelSerializer):

    class Meta:

        model = Customer

        fields = [
            'id',
            'username',
            'email',
            'phone_number',
            'first_name',
            'last_name',
        ]

        # Read only fields cannot be updated
        read_only_fields = [
            'id',
            'username',
            'email',
        ]

# Customer Update Profile Serializer

class CustomerUpdateProfileSerializer(serializers.ModelSerializer):
    class Meta:

        # Connected model
        model = Customer

        # Fields allowed for update
        fields = [

            'phone_number',

            'first_name',

            'last_name',
        ]