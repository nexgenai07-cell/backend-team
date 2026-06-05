from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from .models import Student
from .serializers import StudentSerializer, StudentDetailSerializer

class StudentPagination(PageNumberPagination):
    """
    Custom pagination class enforcing a strict limit of 5 records per page.
    """
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 100


class StudentViewSet(viewsets.ModelViewSet):
    """
    Advanced ModelViewSet for managing Students.
    Implements dynamic serialization, query optimization, filtration, and pagination.
    """
    # Query Optimization: select_related for ForeignKey (Classroom) and prefetch_related for Reverse Foreign Key (Attendance)
    queryset = Student.objects.select_related('classroom').prefetch_related('attendance_records').all()
    pagination_class = StudentPagination
    permission_classes = [IsAuthenticated]
    
    # Adding Search, Filter, and Ordering backends
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['classroom']  # Allows filtering via /api/students/?classroom=1
    search_fields = ['full_name', 'roll_number']  # Allows searching via /api/students/?search=Ali
    ordering_fields = ['full_name', 'roll_number']  # Allows ordering via /api/students/?ordering=full_name

    def get_serializer_class(self):
        """
        Dynamically returns the appropriate serializer based on the current action lifecycle.
        Returns detailed nested structure for 'retrieve' action, and standard layout for others.
        """
        if self.action == 'retrieve':
            return StudentDetailSerializer
        return StudentSerializer