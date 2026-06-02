from rest_framework import serializers
from .models import Product
class ProductSerializer(serializers.ModelSerializer):
    """
    Product Serializer
    Converts Product model data
    into JSON format.
    """
    total_price = serializers.SerializerMethodField()
    stock_status = serializers.SerializerMethodField()
    class Meta:
        model = Product
        fields = [
            'id',
            'name',
            'price',
            'stock',
            'category',
            'description',
            'thumbnail',
            'image',
            'total_price',
            'stock_status'
        ]
    # Calculate total price (price * stock)
    def get_total_price(self, obj):

        """
        Returns total value of stock for product.
        Formula: price * stock
        """
        return obj.price * obj.stock
    
    # Calculate stock status dynamically
    def get_stock_status(self, obj):
        """
        Returns stock availability status.
        """
        if obj.stock > 0:
            return "In Stock"
        return "Out of Stock"

    def validate(self, data):

        """
        Prevent duplicate product with same name + category
        """
        name = data.get('name')
        category = data.get('category')
        if Product.objects.filter(name=name, category=category).exists():
            raise serializers.ValidationError(
                "This product already exists in this category."
            )
        return data