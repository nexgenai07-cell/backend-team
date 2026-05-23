from rest_framework import generics
from .models import Classroom
from .serializers import ClassroomSerializer
from rest_framework.permissions import IsAuthenticated
permission_classes = [IsAuthenticated]


class ClassroomListCreateView(generics.ListCreateAPIView):
    queryset = Classroom.objects.all()
    serializer_class = ClassroomSerializer