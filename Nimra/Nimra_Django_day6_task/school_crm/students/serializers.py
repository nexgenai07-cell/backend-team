from rest_framework import serializers   # DRF serializers import
from .models import Student, Teacher,Class   # Apne models import

# StudentSerializer banaya jo sirf kuch fields ko JSON me convert karega
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
       model = Student
       fields = '__all__'   # includes all fields

# TeacherSerializer banaya jo saare fields ko JSON me convert karega
class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'
        # Custom validation for name
    def validate_name(self, value):
        if not value:   # Agar name empty hai
            raise serializers.ValidationError("This field is required")
        return value

    # Custom validation for email
    def validate_email(self, value):
        if not value:   # Agar email empty hai
            raise serializers.ValidationError("This field is required")
        return value
# Class Serializer → Class model ko JSON me convert karega
class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = '__all__'