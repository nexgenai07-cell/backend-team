from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView

from rest_framework.response import Response

from rest_framework import status

from rest_framework.permissions import IsAuthenticated

from .models import Product

from .serializers import ProductSerializer
class AddProductView(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request):

        serializer = ProductSerializer(
            data=request.data
        )

        if serializer.is_valid():

            serializer.save(
                seller=request.user
            )

            return Response(
                {
                    'message': 'Product Added Successfully'
                },
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
class ProductListView(APIView):

    def get(self, request):

        products = Product.objects.all()

        serializer = ProductSerializer(
            products,
            many=True
        )

        return Response(serializer.data)
class UpdateProductView(APIView):

    permission_classes = [IsAuthenticated]

    def put(self, request, pk):

        try:

            product = Product.objects.get(
                id=pk,
                seller=request.user
            )

        except Product.DoesNotExist:

            return Response(
                {
                    'error': 'Product Not Found'
                },
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = ProductSerializer(
            product,
            data=request.data
        )

        if serializer.is_valid():

            serializer.save(
                seller=request.user
            )

            return Response(
                {
                    'message': 'Product Updated Successfully'
                }
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
class DeleteProductView(APIView):

    permission_classes = [IsAuthenticated]

    def delete(self, request, pk):

        try:

            product = Product.objects.get(
                id=pk,
                seller=request.user
            )

        except Product.DoesNotExist:

            return Response(
                {
                    'error': 'Product Not Found'
                },
                status=status.HTTP_404_NOT_FOUND
            )

        product.delete()

        return Response(
            {
                'message': 'Product Deleted Successfully'
            }
        )