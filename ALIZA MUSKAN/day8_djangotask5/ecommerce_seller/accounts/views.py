from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import SellerRegisterSerializer
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated

class SellerRegisterView(APIView):

    def post(self, request):

        serializer = SellerRegisterSerializer(
            data=request.data
        )

        if serializer.is_valid():

            serializer.save()

            return Response(
                {
                    'message': 'Seller Registered Successfully'
                },
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
    
class SellerLoginView(APIView):

    def post(self, request):

        username = request.data.get('username')

        password = request.data.get('password')

        user = authenticate(
            username=username,
            password=password
        )

        if user is not None:

            refresh = RefreshToken.for_user(user)

            return Response({

                'access_token': str(refresh.access_token),

                'refresh_token': str(refresh)

            })

        return Response(
            {
                'error': 'Invalid Credentials'
            },
            status=status.HTTP_401_UNAUTHORIZED
        )
class SellerDashboardView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):

        return Response({

            'message': 'Welcome Seller Dashboard',

            'seller': request.user.username

        })
