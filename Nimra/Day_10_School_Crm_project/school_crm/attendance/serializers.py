from rest_framework import serializers
from .models import Attendance   # Attendance model import kiya taake serializer usko JSON mein convert kar sake

# ✅ AttendanceSerializer (CRUD ke liye)
class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance        # Ye batata hai ki serializer Attendance model ke liye bana hai
        fields = '__all__'        # '__all__' ka matlab hai model ke saare fields API response mein include honge
from students.models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'full_name', 'roll_number']

class AttendanceSerializer(serializers.ModelSerializer):
    student = StudentSerializer()   # Nested student detail

    class Meta:
        model = Attendance
        fields = ['id', 'student', 'date', 'status']
    # Ab Attendance ke response mein Attendance detail + Student detail dono ek sath aaenge
