from rest_framework import serializers
from .models import Order

# Import existing serializers to handle nested read representations
from users.serializers import StudentSerializer
from products.serializers import ProductSerializer

# Import models required for PrimaryKeyRelatedField lookups during write operations
from users.models import Student
from products.models import Product


class OrderSerializer(serializers.ModelSerializer):
    """
    Serializer for the Order model.
    
    Handles detailed read representations (nested objects) and 
    efficient write operations (using primary keys).
    """

    # Displays full student details when reading; marked as read-only for security
    customer = StudentSerializer(read_only=True)

    # Displays a list of full product details for the order
    products = ProductSerializer(many=True, read_only=True)

    # Accepts a Student ID during creation/update; mapped to the 'customer' field
    customer_id = serializers.PrimaryKeyRelatedField(
        queryset=Student.objects.all(),
        source='customer',
        write_only=True
    )

    # Accepts a list of Product IDs during creation/update; mapped to 'products'
    product_ids = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all(),
        many=True,
        source='products',
        write_only=True
    )

    # Custom field to dynamically calculate the total price of the order
    total_amount = serializers.SerializerMethodField()

    class Meta:
        model = Order
        # Explicitly defining fields to control the API response structure
        fields = [
            'id',
            'customer',
            'customer_id',
            'products',
            'product_ids',
            'total_amount',
            'created_at'
        ]

    def get_total_amount(self, obj):
        """
        Logic to calculate the total order amount by summing 
        the prices of all associated products.
        """
        total = 0
        # Iterate through the ManyToMany relationship of the order instance
        for product in obj.products.all():
            total += product.price
            
        return total