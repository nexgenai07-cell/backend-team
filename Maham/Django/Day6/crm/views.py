from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination
from .models import Student, Teacher, Classroom
from .serializers import StudentSerializer, TeacherSerializer, ClassroomSerializer

class CRMStandardPagination(PageNumberPagination):
    """
    CRM app ke liye custom pagination class
    """
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 50


class ClassroomViewSet(viewsets.ModelViewSet):
    """
    Classroom CRUD APIs handle karne ke liye
    """
    queryset = Classroom.objects.all()
    serializer_class = ClassroomSerializer


class TeacherViewSet(viewsets.ModelViewSet):
    """
    Task 2: Teacher ViewSet jo GET, POST, PUT, PATCH, DELETE sab automatically allow karega
    """
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


class StudentViewSet(viewsets.ModelViewSet):
    """
    Task 1: Student API ko ModelViewSet mei convert kiya.
    Task 16: select_related('classroom') use kiya query optimize karne ke liye (N+1 query problem se bachne ke liye).
    Task 18: Pagination, Search, aur Filtering configure ki.
    """
    # select_related database level par foreign key table ke sath JOIN query chalata hai (Optimization)
    queryset = Student.objects.select_related('classroom').all()
    serializer_class = StudentSerializer
    pagination_class = CRMStandardPagination
    
    # Filters backend define karein
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    
    # URL params ke through classroom wise filter karne ke liye (?classroom=1)
    filterset_fields = ['classroom']
    
    # Name aur roll number ke zariye search karne ke liye (?search=ali)
    search_fields = ['name', 'roll_number']