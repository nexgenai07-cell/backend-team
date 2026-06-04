from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Student,Teacher,Classroom
from .serializers import StudentSerializer,TeacherSerializer,ClassroomSerializer
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
class ClassroomViewSet(ModelViewSet):
    queryset = Classroom.objects.select_related('teacher')
    serializer_class = ClassroomSerializer

    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter
    ]
# Search fields
    search_fields = [
        'name',
        'teacher__name'
    ]

    # Ordering fields
    ordering_fields = [
        'id',
        'name'
    ]

    ordering = ['id']
class TeacherViewSet(ModelViewSet):
    """
    TeacherViewSet (ADVANCED)
    Provides full CRUD + advanced API features:
    ✔ Filtering
    ✔ Search
    ✔ Ordering
    ✔ Pagination (global settings)
    """

    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

    #  Filtering backends
    filter_backends = [
        DjangoFilterBackend,   # exact filtering
        SearchFilter,          # search functionality
        OrderingFilter         # sorting
    ]
    filterset_fields = ['age', ]

    # Search functionality
    search_fields = ['name','email']

    # Sorting fields
    ordering_fields = ['id','name','age']

    # Exact filtering fields
    filterset_fields = ['subject', 'experience']

    # Search fields
    search_fields = ['name', 'email', 'subject']

    # Ordering fields
    ordering_fields = ['id', 'name', 'experience']
    ordering = ['id']
class StudentViewSet(ModelViewSet):
    """
    Student ViewSet
    Provides:
    - Full CRUD Operations
    - Filtering
    - Searching
    - Ordering
    - Optimized Queries
    Endpoints:
    GET     -> List students
    GET/id  -> Retrieve single student
    POST    -> Create student
    PUT     -> Update student
    PATCH   -> Partial update
    DELETE  -> Delete student
    """
    serializer_class = StudentSerializer
    def get_queryset(self):
        """
        Optimize database queries.
        Student -> Classroom -> Teacher
        Using select_related because both relationships
        are ForeignKey fields.
        """
        return Student.objects.select_related(
            'classroom',
            'classroom__teacher'
        )
# Enable API filtering, searching and ordering
    filter_backends = [ DjangoFilterBackend, SearchFilter, OrderingFilter]
    # Exact field filtering
    filterset_fields = [ 'age', 'classroom']
    # Search functionality
    search_fields = [ 'name', 'email' ]
    # Sorting fields
    ordering_fields = [ 'id','name','age']
    # Default ordering
    ordering = ['id']