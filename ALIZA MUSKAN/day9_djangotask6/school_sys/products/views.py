from django.shortcuts import render

# Create your views here.
from .models import  Product
from .serializers import  ProductSerializer
# DRF imports
from rest_framework.viewsets import ModelViewSet
from school_sys.pagination import ProductPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter,OrderingFilter
class ProductViewSet(ModelViewSet):
    """
    Product ViewSet
    Provides automatic CRUD operations.
    GET
    POST
    PUT
    PATCH
    DELETE
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # Apply pagination only for products
    pagination_class = ProductPagination
    # Enable filtering
    filter_backends = [DjangoFilterBackend ,SearchFilter ,OrderingFilter ]
    # Fields allowed for filtering
    filterset_fields = ['category', 'stock', 'price']
     #  Search fields (Task 8)
    search_fields = ['name', 'category']
     #  Ordering (Task 9)
    ordering_fields = ['name', 'price', 'stock', 'id']
    # default ordering
    ordering = ['id']