from rest_framework import serializers

from .models import Student,Teacher,Class


class StudentSerializer(serializers.ModelSerializer):

    class Meta:

        model = Student

        fields = '__all__'

    def validate_name(self, value):

        if value == "":

            raise serializers.ValidationError(
                "Name is required"
            )

        return value

class TeacherSerializer(serializers.ModelSerializer):

    class Meta:
        model = Teacher
        fields = '__all__'
class ClassSerializer(serializers.ModelSerializer):

    class Meta:
        model = Class
        fields = '__all__'