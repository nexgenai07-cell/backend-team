from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination
from .models import Product, Order
from .serializers import ProductSerializer, OrderSerializer

class ProductCustomPagination(PageNumberPagination):
    """
    Task 5 & Task 6: Custom Pagination Class jo har page par sirf 5 products limit karegi
    """
    default_page_size = 5
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 20


class ProductViewSet(viewsets.ModelViewSet):
    """
    Task 3, 5, 6, 7, 8, 9, 11: Product ViewSet jo automatic CRUD, upload, 
    custom pagination, filtering, search aur ordering sab handle karega.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = ProductCustomPagination
    
    # Backends for filtering, text search, and sorting
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    
    # Task 7: Filter products by category, price, and stock
    filterset_fields = ['category', 'price', 'stock']
    
    # Task 8: Search products by name and category (?search=iphone)
    search_fields = ['name', 'category']
    
    # Task 9: Sort products by price, stock, and name (?ordering=-price)
    ordering_fields = ['price', 'stock', 'name']


class OrderViewSet(viewsets.ModelViewSet):
    """
    Task 15: Order query optimization using prefetch_related.
    Many-to-Many relation ke data ko fast fetch karne ke liye prefetch_related use hota hai.
    """
    # prefetch_related database se saare products ko aik alag efficient query mei fetch karta hai
    queryset = Order.objects.prefetch_related('products').all()
    serializer_class = OrderSerializer