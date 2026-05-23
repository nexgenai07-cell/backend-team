from django.shortcuts import render
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated

# Models import
from .models import Student, Classroom
from attendance.models import Attendance

# Serializers import
from .serializers import StudentSerializer
from rest_framework import serializers


# ✅ Attendance serializer (nested ke liye)
class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = ['date', 'status']   # Attendance record mein date aur status show hoga


# ✅ Classroom serializer (nested ke liye)
class ClassroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields = ['class_name', 'section']   # Classroom ka basic detail show hoga


# ✅ Final Student serializer with nested Classroom + Attendance
class StudentSerializer(serializers.ModelSerializer):
    classroom = ClassroomSerializer()   # Nested classroom detail
    attendance_records = AttendanceSerializer(many=True, source='attendance_set')
    # attendance_set = reverse relation jo Attendance model ke ForeignKey(Student) se auto generate hota hai

    class Meta:
        model = Student
        fields = [
            'id', 'full_name', 'email', 'age',
            'roll_number', 'profile_image',
            'classroom', 'attendance_records'
        ]


# ✅ StudentViewSet with CRUD, JWT protection, Search, Filter, Ordering, and Query Optimization
class StudentViewSet(viewsets.ModelViewSet):
    # Query optimization: classroom ek hi query mein fetch hoga, attendance efficiently fetch hogi
    queryset = Student.objects.select_related('classroom').prefetch_related('attendance_set')

    serializer_class = StudentSerializer   # Nested serializer use hoga
    permission_classes = [IsAuthenticated] # Sirf logged-in users access karenge (JWT protected)

    # Search, Filter, Ordering enable kiya
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend]

    search_fields = ['full_name', 'roll_number', 'classroom__class_name']  # Search by name, roll, classroom
    filterset_fields = ['classroom', 'age']                                # Filter by classroom, age
    ordering_fields = ['full_name', 'age']                                 # Order by name, age
