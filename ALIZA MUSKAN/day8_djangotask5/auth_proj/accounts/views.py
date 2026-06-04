from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .permissions import IsTeacher,IsStudent,IsAdmin

from .serializers import StudentRegisterSerializer,TeacherRegisterSerializer,ChangePasswordSerializer,UpdateProfileSerializer


class StudentRegisterView(APIView):

    def post(self, request):

        serializer = StudentRegisterSerializer(data=request.data)

        if serializer.is_valid():

            serializer.save()

            return Response(
                {'message': 'Student registered successfully'},
                status=status.HTTP_201_CREATED
            )

        return Response(serializer.errors)
class StudentProfileView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):

        user = request.user

        data = {
            'id': user.id,
            'username': user.username,
            'email': user.email,
            'phone_number': user.phone_number,
        }

        return Response(data)
    
class StudentDashboardView(APIView):

    permission_classes = [IsStudent]

    def get(self, request):

        return Response({
            'message': 'Welcome Student Dashboard'
        })
# task 6
class TeacherRegisterView(APIView):

    def post(self, request):

        serializer = TeacherRegisterSerializer(data=request.data)

        if serializer.is_valid():

            serializer.save()

            return Response(
                {'message': 'Teacher registered successfully'},
                status=status.HTTP_201_CREATED
            )

        return Response(serializer.errors)
    
# class TeacherDashboardView(APIView):

#     permission_classes = [IsAuthenticated]

#     def get(self, request):

#         if request.user.role != 'teacher':

#             return Response(
#                 {'error': 'Only teachers can access dashboard'},
#                 status=status.HTTP_403_FORBIDDEN
#             )

#         return Response({
#             'message': 'Welcome Teacher Dashboard'
#         })
# task 7
class TeacherDashboardView(APIView):

    permission_classes = [IsTeacher]

    def get(self, request):

        return Response({
            'message': 'Welcome Teacher Dashboard'
        })
class AdminDashboardView(APIView):

    permission_classes = [IsAdmin]

    def get(self, request):

        return Response({
            'message': 'Welcome Admin Dashboard'
        })
    # task 8
class AdminProtectedView(APIView):

    permission_classes = [IsAdminUser]

    def get(self, request):

        return Response({
            'message': 'Only admin can access this API'
        })
    # task 9
class ChangePasswordView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = ChangePasswordSerializer(data=request.data)

        if serializer.is_valid():
            user = request.user
            old_password = serializer.validated_data['old_password']
            new_password = serializer.validated_data['new_password']

            if not user.check_password(old_password):
                return Response(
                    {'error': 'Old password is incorrect'},
                    status=status.HTTP_400_BAD_REQUEST
                )

            user.set_password(new_password)
            user.save()

            return Response({
                'message': 'Password updated successfully'
            }, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# task 10
class UpdateProfileView(APIView):

    permission_classes = [IsAuthenticated]

    def put(self, request):

        user = request.user

        serializer = UpdateProfileSerializer(
            user,data=request.data,partial=True
        )

        if serializer.is_valid():

            serializer.save()

            return Response({
                'message': 'Profile updated successfully',
                'data': serializer.data
            })
        return Response(serializer.errors)