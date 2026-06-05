from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Teacher
from .serializers import TeacherSerializer

class TeacherViewSet(viewsets.ModelViewSet):
    """
    A professional ViewSet that automatically provides standard CRUD actions
    for Teacher management using DRF's ModelViewSet architecture.
    """
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = [IsAuthenticated] # Secure endpoint, requires JWT token [cite: 46]