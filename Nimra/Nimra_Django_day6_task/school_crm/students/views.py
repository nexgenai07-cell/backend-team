
# isi file me likhna sahi jagah hai kyunki views.py
#  ka kaam hota hai request handle karna aur response dena.
# Create your views here.
# DRF ke base classes import karte hain
# DRF ke base classes import karte hain
# DRF base classes import karte hain
from rest_framework.views import APIView       # APIView base class (GET/POST/PUT/DELETE handle karne ke liye)
from rest_framework.response import Response   # Response class (JSON response bhejne ke liye)
from rest_framework import status              # Status codes (200, 201, 400, 404 etc.)
from .models import Student, Teacher, Class    # Models import (Student, Teacher, Class)
from .serializers import StudentSerializer, TeacherSerializer, ClassSerializer  # Serializers import

# -------------------------------
# Student List API → GET request
# -------------------------------
class StudentListView(APIView):
    def get(self, request):
        students = Student.objects.all()   # Saare students fetch karo
        serializer = StudentSerializer(students, many=True)   # List ko serialize karo
        return Response(serializer.data, status=status.HTTP_200_OK)   # 200 OK response

# -------------------------------
# Student Create API → POST request
# -------------------------------
class StudentCreateView(APIView):
    def post(self, request):
        serializer = StudentSerializer(data=request.data)   # Request data serialize karo
        if serializer.is_valid():   # Agar data valid hai
            serializer.save()       # Database me save karo
            return Response({"message": "Student created successfully"}, status=status.HTTP_201_CREATED)  # 201 Created
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)   # Agar error ho to 400 Bad Request

# -------------------------------
# Teacher API → GET + POST
# -------------------------------
class TeacherAPIView(APIView):
    def get(self, request):
        teachers = Teacher.objects.all()   # Saare teachers fetch karo
        serializer = TeacherSerializer(teachers, many=True)   # Serialize karo
        return Response(serializer.data, status=status.HTTP_200_OK)   # 200 OK

    def post(self, request):
        serializer = TeacherSerializer(data=request.data)   # Request data serialize karo
        if serializer.is_valid():
            serializer.save()   # Save new teacher
            return Response(serializer.data, status=status.HTTP_201_CREATED)   # 201 Created
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)   # 400 Bad Request

# -------------------------------
# Student Detail API → GET by ID
# -------------------------------
class StudentDetailAPIView(APIView):
    def get(self, request, pk):
        try:
            student = Student.objects.get(pk=pk)   # Database se student fetch karo by ID
        except Student.DoesNotExist:
            return Response({"error": "Student not found"}, status=status.HTTP_404_NOT_FOUND)   # 404 Not Found
        serializer = StudentSerializer(student)   # Single student serialize karo
        return Response(serializer.data, status=status.HTTP_200_OK)   # 200 OK

# -------------------------------
# Class API → GET + POST
# -------------------------------
class ClassAPIView(APIView):
    def get(self, request):
        classes = Class.objects.all()   # Saare classes fetch karo
        serializer = ClassSerializer(classes, many=True)   # Serialize karo
        return Response(serializer.data, status=status.HTTP_200_OK)   # 200 OK

    def post(self, request):
        serializer = ClassSerializer(data=request.data)   # Request data serialize karo
        if serializer.is_valid():
            serializer.save()   # Save new class
            return Response(serializer.data, status=status.HTTP_201_CREATED)   # 201 Created
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)   # 400 Bad Request
