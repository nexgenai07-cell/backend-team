from rest_framework import serializers
from .models import Student
from classrooms.serializers import ClassroomSerializer
from attendance.serializers import AttendanceSerializer  # Importing AttendanceSerializer for nesting

class StudentSerializer(serializers.ModelSerializer):
    """
    Standard Serializer for basic Student CRUD operations.
    """
    class Meta:
        model = Student
        fields = '__all__'

class StudentDetailSerializer(serializers.ModelSerializer):
    """
    Specialized Nested Serializer for Single Student Detail API response.
    Includes full Classroom details and list of Attendance records.
    """
    # Nested representation for relational data fields
    classroom = ClassroomSerializer(read_only=True)
    
    # Fetching related attendance records using the related_name from Attendance model
    attendance_records = AttendanceSerializer(many=True, read_only=True)

    class Meta:
        model = Student
        fields = ['id', 'full_name', 'email', 'age', 'roll_number', 'profile_image', 
                  'classroom', 'attendance_records']