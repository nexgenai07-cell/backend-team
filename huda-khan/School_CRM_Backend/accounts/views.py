# Import APIView for custom API logic
from rest_framework.views import APIView

# Import Response for sending responses
from rest_framework.response import Response

# Import status codes (201, 400, etc.)
from rest_framework import status

# Import permissions
from rest_framework.permissions import IsAuthenticated

# Import serializer
from .serializers import RegisterSerializer

from rest_framework.permissions import IsAuthenticated
permission_classes = [IsAuthenticated]


# 🔹 Register API
class RegisterView(APIView):

    def post(self, request):

        # Pass request data to serializer
        serializer = RegisterSerializer(data=request.data)

        # Validate data
        if serializer.is_valid():

            # Save user in database
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        # Return errors if invalid
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# 🔹 Profile API (Protected)
class ProfileView(APIView):

    # Only logged-in users can access
    permission_classes = [IsAuthenticated]

    def get(self, request):

        user = request.user

        return Response({
            "username": user.username,
            "email": user.email,
            "role": user.role
        })