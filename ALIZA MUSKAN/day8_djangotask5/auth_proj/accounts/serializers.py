from rest_framework import serializers
from .models import Student

class StudentRegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = ['username', 'email', 'password', 'phone_number']

        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):

        password = validated_data.pop('password')

        user = Student(**validated_data)

        user.set_password(password)

        user.save()

        return user
# task 6
class TeacherRegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = ['username', 'email', 'password', 'phone_number']

        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password')
        teacher = Student(
            role='teacher',  **validated_data)
        teacher.set_password(password)
        teacher.save()
        return teacher
    # task 9
class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(write_only=True, required=True)
    new_password = serializers.CharField(write_only=True, required=True)
# task 10
class UpdateProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = [
            'username',
            'email',
            'phone_number',
            'role',
            'first_name',
            'last_name',
        ]
        read_only_fields = ['role']