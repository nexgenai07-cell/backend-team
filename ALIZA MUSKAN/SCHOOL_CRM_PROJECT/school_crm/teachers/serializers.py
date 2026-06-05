from rest_framework import serializers
from .models import Teacher

class TeacherSerializer(serializers.ModelSerializer):
    """
    Serializer to map Teacher model data into JSON format for CRUD operations.
    """
    class Meta:
        model = Teacher
        fields = '__all__' # [cite: 128]