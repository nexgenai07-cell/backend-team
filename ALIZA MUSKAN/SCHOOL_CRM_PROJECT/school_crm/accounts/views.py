from django.shortcuts import render
from rest_framework import status, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth import get_user_model
from .serializers import RegisterSerializer, UserProfileSerializer

User = get_user_model()

class RegisterView(generics.CreateAPIView):
    """
    API endpoint that allows new users to register.
    Accessible by anyone (unauthenticated users).
    """
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]


class UserProfileView(APIView):
    """
    API endpoint to retrieve or update the authenticated user's profile information.
    Requires a valid JWT Bearer token.
    """
    permission_classes = [IsAuthenticated]

    def get(self, request):
        """
        Handles HTTP GET request to fetch current user data.
        """
        serializer = UserProfileSerializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request):
        """
        Handles HTTP PUT request to perform a full update of the user profile.
        Supports multipart/form-data for profile picture uploads.
        """
        serializer = UserProfileSerializer(request.user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
