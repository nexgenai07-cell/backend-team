from django.shortcuts import render

# Create your views here.
# StudentViewSet = handles all the API requests for Student model (list, create, retrieve, update, delete)
from rest_framework import viewsets,filters
from .models import Student,Teacher,Product,Order
from .serializers import StudentSerializer,TeacherSerializer,ProductSerializer

# ModelViewSet = auto CRUD (GET, POST, PUT, PATCH, DELETE)
class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
# TeacherViewSet = handles all the API requests for Teacher model (list, create, retrieve, update, delete)
class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
# product viewset = handles all the API requests for Product model (list, create, retrieve, update, delete)
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

from django_filters.rest_framework import DjangoFilterBackend

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend,filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['category', 'price']  # ✅ filterable fields
    ordering_fields = ['price', 'stock']
    ordering = ['price']  # default ordering by price

from .serializers import OrderSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
class OrderViewSet(viewsets.ModelViewSet):
     #  select_related → foreign key (customer) ke liye single query
    #  prefetch_related → many-to-many (products) ke liye optimized query
    queryset = Order.objects.select_related('customer').prefetch_related('products')
    serializer_class = OrderSerializer
class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.select_related('classroom').all()
    serializer_class = StudentSerializer
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    # ✅ Filtering, Searching, Ordering enable karna
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    # ✅ Filtering by category
    filterset_fields = ['category']

    # ✅ Search by name or description
    search_fields = ['name', 'description']

    # ✅ Ordering by price or stock
    ordering_fields = ['price', 'stock']
    ordering = ['price']  # default ordering