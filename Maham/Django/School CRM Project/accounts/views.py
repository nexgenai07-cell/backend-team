from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from .serializers import RegisterSerializer, UserProfileSerializer

# ========================================================
# 1. REGISTER USER VIEW (Open for Everyone)
# ========================================================
class RegisterView(APIView):
    permission_classes = [AllowAny] # Is API ko koi bhi use kar sakta hai bina token ke

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "message": "User successfully registered!",
                "user": serializer.data
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# ========================================================
# 2. LOGIN VIEW WITH JWT (Generates Access & Refresh Tokens)
# ========================================================
class LoginView(APIView):
    permission_classes = [AllowAny] # Login ke liye token ki zaroorat nahi hoti

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        
        # User ko email aur password se authenticate karna
        user = authenticate(email=email, password=password)
        
        if user is not None:
            # Simple JWT se tokens generate karna
            refresh = RefreshToken.for_user(user)
            return Response({
                "message": "Login Successful!",
                "access": str(refresh.access_token), # Ye token har API request ke header mei jayega
                "refresh": str(refresh),
                "role": user.role
            }, status=status.HTTP_200_OK)
            
        return Response({"error": "Invalid Email or Password!"}, status=status.HTTP_401_UNAUTHORIZED)

# ========================================================
# 3. USER PROFILE VIEW (Protected Endpoint)
# ========================================================
class ProfileView(APIView):
    permission_classes = [IsAuthenticated] # Sirf login hue users (with valid token) hi isay dekh sakte hain

    def get(self, request):
        # request.user mei current login user ka data hota hai
        serializer = UserProfileSerializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)