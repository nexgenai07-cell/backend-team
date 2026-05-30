from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView

from rest_framework.response import Response

from rest_framework import status

from rest_framework.permissions import (IsAuthenticated,IsAdminUser)

from django.contrib.auth import authenticate

from rest_framework_simplejwt.tokens import RefreshToken

from .models import CustomUser

from .serializers import ( RegisterSerializer, ProfileSerializer)
class RegisterView(APIView):

    def post(self, request):

        serializer = RegisterSerializer(data=request.data)

        if serializer.is_valid():

            serializer.save()

            return Response(
                {
                    'message': 'User Registered Successfully'
                },
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
class LoginView(APIView):

    def post(self, request):

        username = request.data.get( 'username' )

        password = request.data.get( 'password')

        # User authentication
        user = authenticate( username=username, password=password  )

        if user is not None:
            # JWT token generation
            refresh = RefreshToken.for_user(user)
            return Response({
                'access_token': str(refresh.access_token),'refresh_token': str( refresh ), 'role': user.role
            })

        return Response(
            {
                'error': 'Invalid Credentials'
            },
            status=status.HTTP_401_UNAUTHORIZED
        )
class ProfileView(APIView):

    # Protected API
    permission_classes = [IsAuthenticated]
    def get(self, request):

        serializer = ProfileSerializer(
            request.user
        )
        return Response(serializer.data)
class AllUsersView(APIView):
    # Sirf admin access karega
    permission_classes = [IsAdminUser]
    def get(self, request):
        users = CustomUser.objects.all()
        serializer = ProfileSerializer( users,many=True  )
        return Response(serializer.data)