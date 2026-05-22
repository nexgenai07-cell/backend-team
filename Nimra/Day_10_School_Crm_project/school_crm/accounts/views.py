from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from accounts.models import CustomUser   # ✅ CustomUser import kiya (instead of default User)
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.token_blacklist.models import BlacklistedToken, OutstandingToken

# ✅ Register API
class RegisterView(APIView):
    def post(self, request):
        # User data le lo
        username = request.data.get("username")
        password = request.data.get("password")
        role = request.data.get("role", "student")   # Default role student rakha
        phone = request.data.get("phone")
        address = request.data.get("address")

        # User create karo
        user = CustomUser.objects.create_user(
            username=username,
            password=password,
            role=role,
            phone=phone,
            address=address
        )

        return Response({"message": "User registered successfully"}, status=status.HTTP_201_CREATED)


# ✅ Login API
class LoginView(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        try:
            user = CustomUser.objects.get(username=username)
            if user.check_password(password):
                # JWT tokens generate karo
                refresh = RefreshToken.for_user(user)
                return Response({
                    "refresh": str(refresh),
                    "access": str(refresh.access_token),
                    "role": user.role,   # Role bhi response mein aaega
                })
            else:
                return Response({"error": "Invalid password"}, status=status.HTTP_400_BAD_REQUEST)
        except CustomUser.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)


# ✅ Profile API (JWT protected)
class ProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Logged-in user ka detail fetch karo
        user = request.user
        return Response({
            "username": user.username,
            "email": user.email,
            "role": user.role,
            "phone": user.phone,
            "address": user.address
        })

    def post(self, request):
        # Profile update karo
        user = request.user
        email = request.data.get("email")
        phone = request.data.get("phone")
        address = request.data.get("address")

        if email:
            user.email = email
        if phone:
            user.phone = phone
        if address:
            user.address = address

        user.save()
        
        return Response({
            "message": "Profile updated successfully",
            "username": user.username,
            "email": user.email,
            "role": user.role,
            "phone": user.phone,
            "address": user.address
        })


# ✅ Logout API (JWT protected)
class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            # User ke saare active tokens blacklist kar do
            tokens = OutstandingToken.objects.filter(user=request.user)
            for token in tokens:
                BlacklistedToken.objects.get_or_create(token=token)
            return Response({"message": "User logged out successfully"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
