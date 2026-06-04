from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import Cart
from .serializers import CartSerializer

class AddToCartView(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request):

        serializer = CartSerializer(
            data=request.data
        )

        if serializer.is_valid():

            serializer.save(
                user=request.user
            )

            return Response(
                {
                    'message': 'Product Added To Cart'
                },
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
class ViewCartView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):

        cart_items = Cart.objects.filter(
            user=request.user
        )

        serializer = CartSerializer(
            cart_items,
            many=True
        )

        return Response(serializer.data)
class RemoveFromCartView(APIView):

    permission_classes = [IsAuthenticated]

    def delete(self, request, pk):

        try:

            cart_item = Cart.objects.get(
                id=pk,
                user=request.user
            )

        except Cart.DoesNotExist:

            return Response(
                {
                    'error': 'Cart Item Not Found'
                },
                status=status.HTTP_404_NOT_FOUND
            )

        cart_item.delete()

        return Response(
            {
                'message': 'Item Removed From Cart'
            }
        )