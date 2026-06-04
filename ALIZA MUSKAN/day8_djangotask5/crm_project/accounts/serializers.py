from rest_framework import serializers
from .models import CustomUser
# REGISTER SERIALIZER
class RegisterSerializer(serializers.ModelSerializer):

    class Meta:

        model = CustomUser

        fields = [
            'username',
            'email',
            'password',
            'role',
            'phone_number'
        ]

        # Password hide
        extra_kwargs = {

            'password': {
                'write_only': True
            }
        }
    # User create method
    def create(self, validated_data):

        user = CustomUser.objects.create_user(

            username=validated_data['username'],

            email=validated_data['email'],

            password=validated_data['password'],

            role=validated_data['role'],

            phone_number=validated_data['phone_number']
        )

        return user

# PROFILE SERIALIZER
class ProfileSerializer(serializers.ModelSerializer):

    class Meta:

        model = CustomUser

        fields = [
            'id',
            'username',
            'email',
            'role',
            'phone_number'
        ]