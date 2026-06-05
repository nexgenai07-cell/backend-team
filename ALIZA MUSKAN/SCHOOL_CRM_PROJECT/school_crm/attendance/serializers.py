from rest_framework import serializers
from .models import Attendance

class AttendanceSerializer(serializers.ModelSerializer):
    """
    Serializer to map Attendance data into JSON format for CRUD operations.
    """
    class Meta:
        model = Attendance
        fields = '__all__'  # Includes id, student, date, and status