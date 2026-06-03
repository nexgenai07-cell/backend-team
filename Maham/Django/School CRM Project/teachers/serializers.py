from rest_framework import serializers
from .models import Teacher

# ========================================================
# TEACHER SERIALIZER (Data ko JSON or Form-Data mei badalne k liye)
# ========================================================
class TeacherSerializer(serializers.ModelSerializer):
    # User ki details read-only dikhane ke liye (Optional but good)
    username = serializers.ReadOnlyField(source='user.username')
    email = serializers.ReadOnlyField(source='user.email')

    class Meta:
        model = Teacher
        fields = ['id', 'user', 'username', 'email', 'subject', 'phone', 'profile_image']