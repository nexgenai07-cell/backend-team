from rest_framework import serializers
from .models import Classroom   # Classroom model import kiya taake serializer usko JSON mein convert kar sake

class ClassroomSerializer(serializers.ModelSerializer):
    # ModelSerializer ek shortcut hai jo Classroom model ke fields ko JSON mein convert karega
    class Meta:
        model = Classroom        # Ye batata hai ki serializer Classroom model ke liye bana hai
        fields = '__all__'       # '__all__' ka matlab hai model ke saare fields API response mein include honge
from teachers.models import Teacher
# Classroom ke response mein teacher ka detail bhi dikhna chahiye.
class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['id', 'full_name', 'email', 'subject']

class ClassroomSerializer(serializers.ModelSerializer):
    class_teacher = TeacherSerializer()   # Nested teacher detail

    class Meta:
        model = Classroom
        fields = ['id', 'class_name', 'section', 'room_number', 'class_teacher']
