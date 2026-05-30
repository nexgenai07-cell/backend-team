from django.shortcuts import render
# Import Django authentication system
from django.contrib.auth import authenticate
# Import DRF APIView class
from rest_framework.views import APIView
# Import DRF Response class
from rest_framework.response import Response
# Import HTTP status codes
from rest_framework import status
# Import permission classes
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
)
# Import JWT token generator
from rest_framework_simplejwt.tokens import RefreshToken
# Import serializers
from .serializers import (

    CustomerRegistrationSerializer,
    CustomerLoginSerializer,
    CustomerProfileSerializer,
    CustomerUpdateProfileSerializer,
)

# Customer Registration API
class CustomerRegisterAPIView(APIView):

    # Public API
    permission_classes = [AllowAny]

    def post(self, request):

        # Send request data to serializer
        serializer = CustomerRegistrationSerializer(
            data=request.data
        )

        # Check validations
        if serializer.is_valid():

            # Save customer
            serializer.save()

            return Response(

                {
                    'message': 'Customer registered successfully'
                },

                status=status.HTTP_201_CREATED
            )

        # Return validation errors
        return Response(

            serializer.errors,

            status=status.HTTP_400_BAD_REQUEST
        )
# Customer Login API

class CustomerLoginAPIView(APIView):

    # Public API
    permission_classes = [AllowAny]

    def post(self, request):

        # Validate login data
        serializer = CustomerLoginSerializer(
            data=request.data
        )

        # Check validation
        if serializer.is_valid():

            # Get validated username
            username = serializer.validated_data['username']

            # Get validated password
            password = serializer.validated_data['password']

            # Authenticate user
            user = authenticate(

                username=username,

                password=password
            )

            # Check valid user
            if user is not None:

                # Generate refresh token
                refresh = RefreshToken.for_user(user)

                return Response(

                    {

                        'message': 'Login successful',

                        'refresh': str(refresh),

                        'access': str(refresh.access_token),

                    },

                    status=status.HTTP_200_OK
                )

            # Invalid credentials
            return Response(

                {
                    'error': 'Invalid username or password'
                },

                status=status.HTTP_401_UNAUTHORIZED
            )

        # Validation errors
        return Response(

            serializer.errors,

            status=status.HTTP_400_BAD_REQUEST
        )
# Customer Profile API
class CustomerProfileAPIView(APIView):

    # Protected API
    permission_classes = [IsAuthenticated]

    def get(self, request):

        # request.user gives current logged-in user
        serializer = CustomerProfileSerializer(
            request.user
        )

        return Response(

            {

                'message': 'Profile fetched successfully',

                'data': serializer.data
            },

            status=status.HTTP_200_OK
        )


# Customer Update Profile API
class CustomerUpdateProfileAPIView(APIView):

    # Protected API
    permission_classes = [IsAuthenticated]

    def put(self, request):

        # Update logged-in user profile
        serializer = CustomerUpdateProfileSerializer(

            request.user,

            data=request.data,

            partial=True
        )

        # Validate update data
        if serializer.is_valid():

            # Save updated data
            serializer.save()

            return Response(

                {

                    'message': 'Profile updated successfully',

                    'data': serializer.data
                },

                status=status.HTTP_200_OK
            )

        # Return validation errors
        return Response(

            serializer.errors,

            status=status.HTTP_400_BAD_REQUEST
        )
