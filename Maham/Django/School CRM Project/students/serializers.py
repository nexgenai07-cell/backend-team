from rest_framework import serializers
from .models import Student
from classrooms.serializers import ClassroomSerializer
from attendance.serializers import AttendanceSerializer # Naya import kiya

# WRITE SERIALIZER (Same rahega)
class StudentWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'user', 'classroom', 'age', 'roll_number', 'profile_image']

# DETAILED SERIALIZER (Is mei attendance_records jor di hain)
class StudentDetailSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source='user.username')
    email = serializers.ReadOnlyField(source='user.email')
    classroom = ClassroomSerializer(read_only=True)
    
    # ⚡ Nested Requirement: Student ke andar us ke saare attendance records automatically dikhenge
    attendance_records = AttendanceSerializer(many=True, read_only=True)

    class Meta:
        model = Student
        fields = ['id', 'user', 'username', 'email', 'classroom', 'age', 'roll_number', 'profile_image', 'attendance_records']