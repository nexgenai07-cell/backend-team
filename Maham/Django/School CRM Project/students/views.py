from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

from .models import Student
from .serializers import StudentWriteSerializer, StudentDetailSerializer
from classrooms.views import IsAdminOrReadOnly

# ========================================================
# CUSTOM PAGINATION (Har page par 5 students dikhane k liye)
# ========================================================
class StudentPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 20

# ========================================================
# STUDENT VIEWSET (CRUD, Search, Filter aur Query Optimization)
# ========================================================
class StudentViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly]
    pagination_class = StudentPagination
    
    # Filter backends set kiye hain jese PDF mei required hai
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['classroom', 'age'] # Classroom aur Age wise filter karne ke liye
    search_fields = ['user__username', 'roll_number'] # Username aur Roll Number se search karne ke liye
    ordering_fields = ['age', 'roll_number'] # Sorting/Ordering karne ke liye

    def get_queryset(self):
        # ⚡ Query Optimization: select_related se SQL Joins lagte hain aur database par load nahi parta
        return Student.objects.select_related('user', 'classroom').all()

    def get_serializer_class(self):
        # Agar request GET (list/detail) hai to Nested/Detail Serializer use hoga
        if self.request.method == 'GET':
            return StudentDetailSerializer
        # Create, Update, Delete ke liye simple serializer use hoga
        return StudentWriteSerializer