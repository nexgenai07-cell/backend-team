from rest_framework import serializers
from .models import Student, Teacher, Classroom

class ClassroomSerializer(serializers.ModelSerializer):
    """
    Classroom ke saare fields ko JSON mei convert karne ke liye
    """
    class Meta:
        model = Classroom
        fields = '__all__'  # Is se saare fields (id, name, section) automatically include ho jayenge


class TeacherSerializer(serializers.ModelSerializer):
    """
    Task 2: Teacher ViewSet ke liye proper serializer
    """
    class Meta:
        model = Teacher
        fields = '__all__'  # Teacher ke saare fields automatically map ho jayenge


class StudentSerializer(serializers.ModelSerializer):
    """
    Task 1 & Task 10: Student API ke liye serializer jo image upload ko handle karega
    """
    class Meta:
        model = Student
        fields = '__all__'  # Is mei 'profile_image' ka field bhi automatically handle ho jayega