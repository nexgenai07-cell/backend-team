from rest_framework import serializers
from .models import Student,Teacher,Classroom
class TeacherSerializer(serializers.ModelSerializer):
    """
    Teacher Serializer
    Converts model data into JSON and validates input
    """

    class Meta:
        model = Teacher
        fields = '__all__'
class ClassroomSerializer(serializers.ModelSerializer):
    """
    Classroom Serializer
    - Accepts teacher_id for POST/PUT
    - Shows full teacher details in response
    """

    teacher = TeacherSerializer(read_only=True)
    teacher_id = serializers.PrimaryKeyRelatedField(
        queryset=Teacher.objects.all(),
        source='teacher',
        write_only=True
    )

    class Meta:
        model = Classroom
        fields = '__all__'
class StudentSerializer(serializers.ModelSerializer):
    """
    Student Serializer
    Converts Student model data into JSON format
    and validates incoming API data.
    """
    """
    Student Serializer (CRM Enhanced)

    Shows:
    - Student details
    - Classroom + Teacher nested data
    """

    classroom = ClassroomSerializer(read_only=True)
    class Meta:
        model = Student
        fields = '__all__'

