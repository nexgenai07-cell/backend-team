from rest_framework import serializers
from .models import Teacher   # Teacher model import kiya taake serializer usko JSON mein convert kar sake

# ✅ Serializer model ko JSON mein convert karega aur Postman ke response mein data dikhayega
class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher        # Ye batata hai ki serializer Teacher model ke liye bana hai
        fields = '__all__'     # '__all__' ka matlab hai model ke saare fields API response mein include honge
from classrooms.models import Classroom

class ClassroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields = ['id', 'class_name', 'section', 'room_number']

class TeacherSerializer(serializers.ModelSerializer):
    classrooms = ClassroomSerializer(many=True, source='classroom_set')  
    # classroom_set = reverse relation jo Classroom model ke ForeignKey(Teacher) se auto generate hota hai

    class Meta:
        model = Teacher
        fields = ['id', 'full_name', 'email', 'subject', 'salary', 'profile_image', 'classrooms']
