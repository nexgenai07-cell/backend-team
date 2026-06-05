from rest_framework import serializers
from .models import Classroom

class ClassroomSerializer(serializers.ModelSerializer):
    """
    Serializer to handle Classroom data serialization and deserialization.
    """
    class Meta:
        model = Classroom
        fields = '__all__' 