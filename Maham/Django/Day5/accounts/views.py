from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from .models import Product, CartItem, Order
from .serializers import ProductSerializer, CartItemSerializer, OrderSerializer
from .permissions import IsSellerRole, IsCustomerRole

# Saare Serializers yahan aik sath import kar diye hain
from .serializers import (
    UserRegistrationSerializer, 
    UserProfileSerializer, 
    ChangePasswordSerializer, 
    UpdateProfileSerializer
)
from .permissions import IsTeacherRole, IsStudentRole

# ==========================================
# TASK 1: USER REGISTRATION API
# ==========================================
class RegisterView(APIView):
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User registered successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# ==========================================
# TASK 2: LOGIN API (JWT GENERATION)
# ==========================================
class LoginView(APIView):
    def post(self, request):
        username_or_email = request.data.get('username') or request.data.get('email')
        password = request.data.get('password')

        if not username_or_email or not password:
            return Response({"error": "Please provide both credentials"}, status=status.HTTP_400_BAD_REQUEST)

        from django.contrib.auth import get_user_model
        User = get_user_model()
        
        try:
            if '@' in username_or_email:
                user_obj = User.objects.get(email=username_or_email)
                username = user_obj.username
            else:
                username = username_or_email
        except User.DoesNotExist:
            return Response({"detail": "Invalid Credentials"}, status=status.HTTP_401_UNAUTHORIZED)

        user = authenticate(username=username, password=password)

        if user is not None:
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }, status=status.HTTP_200_OK)
        
        return Response({"detail": "Invalid Credentials"}, status=status.HTTP_401_UNAUTHORIZED)


# ==========================================
# TASK 3 & 4: PROTECTED PROFILE API
# ==========================================
class ProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserProfileSerializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)


# ==========================================
# TASK 5: STUDENT PROFILE API
# ==========================================
class StudentProfileView(APIView):
    permission_classes = [IsAuthenticated, IsStudentRole]

    def get(self, request):
        serializer = UserProfileSerializer(request.user)
        return Response({
            "message": "Welcome to Student Profile",
            "profile": serializer.data
        }, status=status.HTTP_200_OK)


# ==========================================
# TASK 6: TEACHER DASHBOARD API
# ==========================================
class TeacherDashboardView(APIView):
    permission_classes = [IsAuthenticated, IsTeacherRole]

    def get(self, request):
        return Response({
            "message": f"Welcome Teacher {request.user.username}! Here is your dashboard data."
        }, status=status.HTTP_200_OK)


# ==========================================
# TASK 8: ADMIN PROTECTED API
# ==========================================
class AdminOnlyView(APIView):
    permission_classes = [IsAuthenticated, IsAdminUser]

    def get(self, request):
        return Response({
            "message": "Welcome Admin! This is a highly protected admin-only API."
        }, status=status.HTTP_200_OK)


# ==========================================
# TASK 9: CHANGE PASSWORD API
# ==========================================
class ChangePasswordView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        serializer = ChangePasswordSerializer(data=request.data)

        if serializer.is_valid():
            if not user.check_password(serializer.validated_data['old_password']):
                return Response({"old_password": "Wrong old password."}, status=status.HTTP_400_BAD_REQUEST)
            
            user.set_password(serializer.validated_data['new_password'])
            user.save()
            return Response({"message": "Password updated successfully"}, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# ==========================================
# TASK 10: UPDATE PROFILE API
# ==========================================
class UpdateProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request):
        user = request.user
        serializer = UpdateProfileSerializer(user, data=request.data, partial=True)
        
        if serializer.is_valid():
            serializer.save()
            return Response({
                "message": "Profile updated successfully",
                "profile": serializer.data
            }, status=status.HTTP_200_OK)
            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

# ==========================================
# TASK 13: PROTECTED PRODUCT API
# ==========================================
class ProductListCreateView(APIView):
    # Logged-in users hi dekh sakein, permissions handle ham methods ke andar karenge
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Customers aur Sellers dono dekh sakte hain
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        # Sirf Seller hi product add kar sakta hai
        if request.user.role != 'seller':
            return Response({"detail": "Only sellers can add products."}, status=status.HTTP_03_FORBIDDEN)
        
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(seller=request.user) # Login seller ko assign karna
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# ==========================================
# TASK 14: CART SYSTEM WITH AUTHENTICATION
# ==========================================
class CartAPIView(APIView):
    # Sirf customers hi cart access kar sakein
    permission_classes = [IsAuthenticated, IsCustomerRole]

    def get(self, request):
        # User ko sirf uska apna cart dikhana
        items = CartItem.objects.filter(user=request.user)
        serializer = CartItemSerializer(items, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        # Cart mein item add karna
        serializer = CartItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response({"message": "Product added to cart successfully", "data": serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        # Cart item remove karna (body mein cart item id pass karni hogi)
        cart_item_id = request.data.get('cart_item_id')
        try:
            item = CartItem.objects.get(id=cart_item_id, user=request.user)
            item.delete()
            return Response({"message": "Item removed from cart"}, status=status.HTTP_200_OK)
        except CartItem.DoesNotExist:
            return Response({"error": "Item not found in your cart"}, status=status.HTTP_404_NOT_FOUND)


# ==========================================
# TASK 15: ORDER SYSTEM
# ==========================================
class OrderAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Agar admin hai to saare orders dikhao, warna sirf user ko apne orders dikhao
        if request.user.is_staff or request.user.role == 'admin':
            orders = Order.objects.all()
        else:
            orders = Order.objects.filter(user=request.user)
            
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        # Order place karna customer ke pure cart items se
        cart_items = CartItem.objects.filter(user=request.user)
        if not cart_items.exists():
            return Response({"error": "Your cart is empty. Cannot place order."}, status=status.HTTP_400_BAD_REQUEST)

        # Naya order object banana
        order = Order.objects.create(user=request.user)
        for item in cart_items:
            order.products.add(item.product)
        
        order.save()
        
        # Order place hone ke baad cart empty kar dena
        cart_items.delete()
        
        return Response({"message": "Order placed successfully!", "order_id": order.id}, status=status.HTTP_201_CREATED)