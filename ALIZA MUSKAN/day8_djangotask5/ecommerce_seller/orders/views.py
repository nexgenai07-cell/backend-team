from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import (IsAuthenticated,IsAdminUser)
from .models import Order
from .serializers import OrderSerializer
from products.models import Product

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import Product, Order
from .serializers import OrderSerializer

class PlaceOrderView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        product_id = request.data.get('product')
        # --- Quantity Validation Point ---
        try:
            quantity = int(request.data.get('quantity', 0))
            if quantity <= 0:
                raise ValueError  # Agar quantity 0 ya minus mein ho to error generate karein
        except (ValueError, TypeError):
            return Response(
                {'error': 'Invalid quantity. It must be a positive number.'},
                status=status.HTTP_400_BAD_REQUEST
            )
        # Product check karna
        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return Response(
                {'error': 'Product Not Found'},
                status=status.HTTP_404_NOT_FOUND
            )
        total_price = product.price * quantity
        order = Order.objects.create(
            user=request.user,
            product=product,
            quantity=quantity,
            total_price=total_price
        )
        serializer = OrderSerializer(order)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED
        )
class UserOrdersView(APIView):

    permission_classes = [IsAuthenticated]
    def get(self, request):
        orders = Order.objects.filter(  user=request.user)
        serializer = OrderSerializer(orders,many=True)
        return Response(serializer.data)
class AllOrdersView(APIView):

    permission_classes = [IsAdminUser]

    def get(self, request):
        orders = Order.objects.all()
        serializer = OrderSerializer(  orders, many=True )
        return Response(serializer.data)