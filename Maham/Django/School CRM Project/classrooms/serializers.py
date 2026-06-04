from rest_framework import serializers
from .models import Classroom

# ========================================================
# CLASSROOM SERIALIZER (Data ko JSON mei convert krne k liye)
# ========================================================
class ClassroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields = '__all__' # Saare fields (id, name, section) include ho jayein ge