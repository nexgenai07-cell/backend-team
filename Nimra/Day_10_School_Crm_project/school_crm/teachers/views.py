from django.shortcuts import render
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated

# Teacher model import
from .models import Teacher

# Teacher serializer import
from .serializers import TeacherSerializer


# ✅ TeacherViewSet (CRUD + JWT + Search/Filter/Ordering + Query Optimization)
class TeacherViewSet(viewsets.ModelViewSet):
    # Query optimization: classrooms efficiently fetch honge
    queryset = Teacher.objects.prefetch_related('classroom_set')

    serializer_class = TeacherSerializer
    permission_classes = [IsAuthenticated]   # Sirf logged-in users access karenge (JWT protected)

    # Search, Filter, Ordering enable kiya
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend]

    search_fields = ['full_name', 'email', 'subject']   # Search by name, email, subject
    filterset_fields = ['subject']                      # Filter by subject
    ordering_fields = ['full_name', 'salary']           # Order by name, salary
