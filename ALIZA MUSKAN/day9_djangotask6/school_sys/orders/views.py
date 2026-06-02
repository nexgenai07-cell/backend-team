from django.shortcuts import render
# Create your views here.
from rest_framework.viewsets import ModelViewSet

from .models import Order
from .serializers import OrderSerializer
class OrderViewSet(ModelViewSet):
    """
    ViewSet for handling Order-related CRUD operations.
    Provides endpoints for:
    - Creating an Order
    - Listing all Orders
    - Retrieving a specific Order
    - Updating an Order (PUT/PATCH)
    - Deleting an Order
    """
    # Linking the predefined OrderSerializer to handle input validation and output formatting
    serializer_class = OrderSerializer

    def get_queryset(self):
        """
        Retrieves the base queryset for Orders with optimized database queries.
        Uses select_related and prefetch_related to prevent the N+1 query problem
        by fetching related data in bulk.
        """

        # select_related performs a SQL JOIN to fetch the One-to-Many relationship (customer)
        # prefetch_related executes a separate query to efficiently fetch the Many-to-Many relationship (products)
        return Order.objects.select_related(
            'customer'
        ).prefetch_related(
            'products'
        )