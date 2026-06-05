from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Teacher
from .serializers import TeacherSerializer
from classrooms.views import IsAdminOrReadOnly # Hum ne jo classroom mei permission banayi thi, wahi yahan use kr rhe hain

# ========================================================
# TEACHER VIEWSET (CRUD operations handled automatically)
# ========================================================
class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly] # Login lazmi hai, edit sirf Admin karega