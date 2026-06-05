from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Classroom
from .serializers import ClassroomSerializer

class ClassroomViewSet(viewsets.ModelViewSet):
    """
    ModelViewSet to manage all lifecycle events of school classrooms automatically.
    """
    queryset = Classroom.objects.all()
    serializer_class = ClassroomSerializer
    permission_classes = [IsAuthenticated] # Requires JWT token 