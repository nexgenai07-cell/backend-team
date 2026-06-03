from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

# ========================================================
# 1. USER REGISTRATION SERIALIZER
# ========================================================
class RegisterSerializer(serializers.ModelSerializer):
    # Password ko write_only rakha hai taake ye response mei wapas nazar na aaye
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'role']

    def create(self, validated_data):
        # create_user method password ko automatically hash (secure) kar deta hai
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            role=validated_data.get('role', 'ADMIN') # Default role ADMIN hoga agar na bheja jaye
        )
        return user

# ========================================================
# 2. USER PROFILE SERIALIZER
# ========================================================
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'role']