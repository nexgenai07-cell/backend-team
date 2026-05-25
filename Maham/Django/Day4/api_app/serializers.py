from rest_framework import serializers
from .models import Student, Teacher, Classroom, Attendance, Result, Product, Cart, Order

# Serializer data ko JSON se QuerySet aur QuerySet se JSON mein convert karta hai aur validation karta hai
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        # Yeh serializer hum Student model ke liye bana rahe hain
        model = Student
        
        # '__all__' ka matlab hai ke database ke saare fields (id, name, email, age, class_name) is mein shamil hain
        fields = '__all__'

# Teacher ke data validation aur conversion ke liye serializer
class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'

# Classroom ke data validation aur conversion ke liye serializer
class ClassroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields = '__all__'

# Attendance data ko validation aur format check karne ke liye serializer
class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = '__all__'

# Result data ko validate aur process karne ke liye serializer
class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Result
        fields = '__all__'

# Product data validation aur conversion ke liye
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

# Cart data handle karne ke liye
class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'

# Order submission aur fields matching ke liye
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'