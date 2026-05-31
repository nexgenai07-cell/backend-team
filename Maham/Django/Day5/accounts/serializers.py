from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Product, CartItem, Order

User = get_user_model()

# ==========================================
# TASK 1: USER REGISTRATION SERIALIZER
# ==========================================
class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})
    confirm_password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'confirm_password', 'role']
        extra_kwargs = {'role': {'required': False}}

    def validate(self, attrs):
        if attrs['password'] != attrs['confirm_password']:
            raise serializers.ValidationError({"confirm_password": "Passwords do not match."})
        return attrs

    def create(self, validated_data):
        validated_data.pop('confirm_password')
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)  # Automatically hashes the password safely
        user.save()
        return user


# ==========================================
# TASK 3, 5, 6: USER PROFILE SERIALIZER
# ==========================================
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'role']


# ==========================================
# TASK 9: CHANGE PASSWORD SERIALIZER
# ==========================================
class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True, style={'input_type': 'password'})
    new_password = serializers.CharField(required=True, style={'input_type': 'password'})
    confirm_new_password = serializers.CharField(required=True, style={'input_type': 'password'})

    def validate(self, attrs):
        if attrs['new_password'] != attrs['confirm_new_password']:
            raise serializers.ValidationError({"confirm_new_password": "New passwords do not match."})
        return attrs


# ==========================================
# TASK 10: UPDATE PROFILE SERIALIZER
# ==========================================
class UpdateProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email']
        extra_kwargs = {
            'username': {'required': False},
            'email': {'required': False},
        }

# ==========================================
# TASK 13: PRODUCT SERIALIZER
# ==========================================
class ProductSerializer(serializers.ModelSerializer):
    seller = serializers.ReadOnlyField(source='seller.username')

    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'seller']


# ==========================================
# TASK 14: CART SERIALIZER
# ==========================================
class CartItemSerializer(serializers.ModelSerializer):
    product_name = serializers.ReadOnlyField(source='product.name')
    product_price = serializers.ReadOnlyField(source='product.price')

    class Meta:
        model = CartItem
        fields = ['id', 'product', 'product_name', 'product_price', 'quantity']


# ==========================================
# TASK 15: ORDER SERIALIZER
# ==========================================
class OrderSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    products = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'user', 'products', 'created_at']