from rest_framework import serializers
from .models import Student,Teacher,Product,Order
total_price = serializers.SerializerMethodField()
stock_status = serializers.SerializerMethodField()
# student serializer = converts student model objects to JSON format and vice versa
# Serializer = converts model objects <-> JSON
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'   # include all fields (id, name, age, email)
# teacher serializer = converts teacher model objects to JSON format and vice versa
class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'   # include all fields (id, name, subject, email)
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'stock', 'category', 'description', 'thumbnail', 'image']
 # Calculated fields banana hote hain jo database me directly store nahi hote, but runtime pe calculate hote hain
    def get_total_price(self, obj):
        # Example: price * stock
        return obj.price * obj.stock

    def get_stock_status(self, obj):
        return "In Stock" if obj.stock > 0 else "Out of Stock"
class OrderSerializer(serializers.ModelSerializer):
    customer = StudentSerializer()   # nested serializer
    products = ProductSerializer(many=True)  # nested serializer
    total_amount = serializers.SerializerMethodField()
    # ✅ IDs accept karne ke liye PrimaryKeyRelatedField
    customer = serializers.PrimaryKeyRelatedField(queryset=Student.objects.all())
    products = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(), many=True)


    class Meta:
        model = Order
        fields = ['id', 'customer', 'products', 'total_amount', 'created_at']

    def get_total_amount(self, obj):
        return sum([p.price for p in obj.products.all()])
