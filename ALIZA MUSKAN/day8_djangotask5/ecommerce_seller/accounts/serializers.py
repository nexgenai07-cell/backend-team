from rest_framework import serializers

from .models import CustomUser

from django.contrib.auth.hashers import make_password


class SellerRegisterSerializer(serializers.ModelSerializer):

    class Meta:

        model = CustomUser

        fields = [
            'username',
            'email',
            'password',
            'phone_number'
        ]

        extra_kwargs = { 'password': {'write_only': True} }

    def create(self, validated_data):

        validated_data['password'] = make_password(validated_data['password'] )

        validated_data['role'] = 'seller'

        user = CustomUser.objects.create( **validated_data)

        return user

