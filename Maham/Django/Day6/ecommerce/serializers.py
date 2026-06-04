from rest_framework import serializers
from .models import Product, Order

class ProductSerializer(serializers.ModelSerializer):
    total_price = serializers.SerializerMethodField()
    stock_status = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = [
            'id', 'name', 'price', 'stock', 'category', 'description', 
            'thumbnail', 'product_image', 'total_price', 'stock_status'
        ]

    def get_total_price(self, obj):
        tax_rate = 0.05
        total = float(obj.price) + (float(obj.price) * tax_rate)
        return round(total, 2)

    def get_stock_status(self, obj):
        if obj.stock > 0:
            return "In Stock"
        return "Out of Stock"


class OrderSerializer(serializers.ModelSerializer):
    """
    Task 14: Sahi Writable Nested Serializer logic ke sath.
    """
    # ordered_products sirf output (response) dikhane ke liye hai
    ordered_products = ProductSerializer(source='products', many=True, read_only=True)
    
    # products field input lene ke liye use hoga (Many-to-Many Primary Key Relation)
    products = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all(), 
        many=True, 
        write_only=True  # Ye sirf input lete waqt dikhega, output mei nahi
    )
    
    total_amount = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = ['id', 'customer_name', 'customer_email', 'products', 'ordered_products', 'total_amount', 'created_at']

    def get_total_amount(self, obj):
        return sum(product.price for product in obj.products.all())

    def create(self, validated_data):
        """
        Custom create method jo product list ko order ke sath link karega
        """
        # 1. Validated data se products ki list alag nikal lein
        products_data = validated_data.pop('products', [])
        
        # 2. Pehle order create karein base fields ke sath
        order = Order.objects.create(**validated_data)
        
        # 3. Ab Many-to-Many field mei saare products set/add karein
        order.products.set(products_data)
        
        # 4. Final complete order return karein
        return order