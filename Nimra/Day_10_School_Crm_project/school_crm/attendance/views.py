from django.shortcuts import render

# DRF ke viewsets import kiye (CRUD ke liye)
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated

# Attendance model import kiya
from .models import Attendance

# Attendance serializer import kiya
from .serializers import AttendanceSerializer


# ✅ AttendanceViewSet (CRUD + JWT + Search/Filter/Ordering + Query Optimization)
class AttendanceViewSet(viewsets.ModelViewSet):
    # Query optimization: student ke detail efficiently fetch honge
    queryset = Attendance.objects.select_related('student')

    serializer_class = AttendanceSerializer
    permission_classes = [IsAuthenticated]   # Sirf logged-in users access karenge (JWT protected)

    # Search, Filter, Ordering enable kiya
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend]

    search_fields = ['student__full_name', 'status']   # Search by student name or status
    filterset_fields = ['status', 'date']              # Filter by status or date
    ordering_fields = ['date', 'status']               # Order by date or status
