from rest_framework import serializers
from .models import Student, Classroom   # ✅ sirf Student aur Classroom students app mein hain
from attendance.models import Attendance # ✅ Attendance ko attendance app se import karo
  # Models import kiye taake unke liye serializer ban sake

# Basic Student serializer (sab fields JSON mein convert karne ke liye)
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
    # Ye basic version hai jo sirf Student ke apne fields return karega (full_name, email, age, roll_number, profile_image, classroom_id)

# Classroom serializer (nested ke liye)
class ClassroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields = ['id', 'class_name', 'section', 'room_number']
    # Ye classroom ka detail JSON mein convert karega (id, class_name, section, room_number)

# Student serializer with nested Classroom
class StudentSerializer(serializers.ModelSerializer):
    classroom = ClassroomSerializer()   # Nested serializer use kiya

    class Meta:
        model = Student
        fields = '__all__'
    # Ab Student ke response mein classroom ka detail bhi aaega, sirf ID nahi

# Attendance serializer (nested ke liye)
class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = ['date', 'status']
    # Attendance ka detail JSON mein convert karega (date, status)

# Final Student serializer with Classroom + Attendance nested
class StudentSerializer(serializers.ModelSerializer):
    classroom = ClassroomSerializer()   # Nested classroom detail
    attendance_records = AttendanceSerializer(many=True, source='attendance_set')
    # attendance_set ek reverse relation hai jo Attendance model ke ForeignKey(Student) se auto generate hota hai

    class Meta:
        model = Student
        fields = ['id', 'full_name', 'email', 'age', 'roll_number', 'profile_image', 'classroom', 'attendance_records']
    # Ab Student ke response mein Student detail + Classroom detail + Attendance records sab ek sath aaenge


# Basic StudentSerializer: CRUD ke liye quick JSON conversion.

# ClassroomSerializer: Nested classroom detail dikhane ke liye.

# AttendanceSerializer: Attendance records dikhane ke liye.

# Final StudentSerializer: Requirement ke hisaab se ek hi response mein Student + Classroom + Attendance combine karne ke liye.


