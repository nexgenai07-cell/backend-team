from django.shortcuts import render
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated

# Models import
from .models import Classroom
from teachers.models import Teacher
from students.models import Student

# Serializers import
from rest_framework import serializers


# ✅ Teacher serializer (nested ke liye)
class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['id', 'full_name', 'email', 'subject']
        # Teacher ka basic detail show hoga


# ✅ Student serializer (nested ke liye)
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'full_name', 'roll_number']
        # Classroom ke andar students ka basic detail show hoga


# ✅ Classroom serializer with nested Teacher + Students
class ClassroomSerializer(serializers.ModelSerializer):
    class_teacher = TeacherSerializer()                   # Nested teacher detail
    students = StudentSerializer(many=True, source='student_set')  
    # student_set = reverse relation jo Student model ke ForeignKey(Classroom) se auto generate hota hai

    class Meta:
        model = Classroom
        fields = ['id', 'class_name', 'section', 'room_number', 'class_teacher', 'students']
        # Classroom ke response mein class details + teacher + students sab ek sath aaenge


# ✅ ClassroomViewSet with CRUD, JWT protection, Search, Filter, Ordering, and Query Optimization
class ClassroomViewSet(viewsets.ModelViewSet):
    # Query optimization: teacher ek hi query mein fetch hoga, students efficiently fetch honge
    queryset = Classroom.objects.select_related('class_teacher').prefetch_related('student_set')

    serializer_class = ClassroomSerializer   # Nested serializer use hoga
    permission_classes = [IsAuthenticated]   # Sirf logged-in users access karenge (JWT protected)

    # Search, Filter, Ordering enable kiya
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend]

    search_fields = ['class_name', 'section', 'class_teacher__full_name']  # Search by class, section, teacher name
    filterset_fields = ['class_teacher']                                   # Filter by teacher
    ordering_fields = ['class_name', 'section']                            # Order by class_name, section
