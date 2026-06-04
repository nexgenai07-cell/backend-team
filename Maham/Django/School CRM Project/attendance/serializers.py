from rest_framework import serializers
from .models import Attendance

# ========================================================
# ATTENDANCE SERIALIZER (Attendance data handle krne k liye)
# ========================================================
class AttendanceSerializer(serializers.ModelSerializer):
    # Student ka username read-only field ke tor par show karne ke liye
    student_username = serializers.ReadOnlyField(source='student.user.username')

    class Meta:
        model = Attendance
        fields = ['id', 'student', 'student_username', 'date', 'status']