from rest_framework import generics
from .models import Student
from .serializers import StudentSerializer
from rest_framework.permissions import IsAuthenticated
from accounts.permissions import IsAdminUserRole



class StudentListCreateView(generics.ListCreateAPIView):
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Student.objects.all()
        classroom_id = self.request.query_params.get('classroom')

        if classroom_id:
            queryset = queryset.filter(classroom_id=classroom_id)

        return queryset