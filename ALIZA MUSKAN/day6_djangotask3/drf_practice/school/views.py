from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView

from rest_framework.response import Response

from .models import Student,Teacher,Class

from .serializers import StudentSerializer,TeacherSerializer,ClassSerializer


class StudentAPIView(APIView):

    def get(self, request):

        students = Student.objects.all()

        serializer = StudentSerializer(
            students,
            many=True
        )
        return Response(serializer.data)
    
    def post(self, request):

        serializer = StudentSerializer(data=request.data)

        if serializer.is_valid():

            serializer.save()

            return Response(serializer.data, status=201)

        return Response(serializer.errors, status=400)
# dynamic student API TASK 10ass StudentDetailAPIView(APIView):
class StudentDetailAPIView(APIView):

    def get(self, request, id):

        try:
            student = Student.objects.get(id=id)

        except Student.DoesNotExist:
            return Response(
                {"error": "Student not found"},
                status=404
            )

        serializer = StudentSerializer(student)
        return Response(serializer.data, status=200)
    
class TeacherAPIView(APIView):

    def get(self, request):

        teachers = Teacher.objects.all()

        serializer = TeacherSerializer(teachers, many=True)

        return Response(serializer.data)
    def post(self, request):

        serializer = TeacherSerializer(data=request.data)

        if serializer.is_valid():

            serializer.save()

            return Response(serializer.data, status=201)

        return Response(serializer.errors, status=400)
    
class ClassAPIView(APIView):

    def get(self, request):
        classes = Class.objects.all()
        serializer = ClassSerializer(classes, many=True)
        return Response(serializer.data)

    def post(self, request):

        serializer = ClassSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)

        return Response(serializer.errors, status=400)