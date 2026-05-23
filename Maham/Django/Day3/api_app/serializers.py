from rest_framework import serializers
from .models import Student, Teacher, Class

# Task 2 & Task 8: Student Serializer with Validation
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

    # Custom validation check karne ke liye method (Task 8)
    def validate(self, data):
        # Agar name blank/khali bheja jaye
        if 'name' in data and not data['name']:
            raise serializers.ValidationError({"error": "This field is required"})
        # Agar email blank/khali bheja jaye
        if 'email' in data and not data['email']:
            raise serializers.ValidationError({"error": "This field is required"})
        return data

# Task 3: Teacher Serializer
class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'

# Task 12: Class Serializer
class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = '__all__'