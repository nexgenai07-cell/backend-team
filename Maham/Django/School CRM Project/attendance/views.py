from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, BasePermission, SAFE_METHODS
from .models import Attendance
from .serializers import AttendanceSerializer

# ========================================================
# CUSTOM PERMISSION (Sirf Admin or Teacher ko attendance lagane ki ijazat)
# ========================================================
class IsAdminOrTeacherOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        # Agar sirf dekhna (GET request) hai to login hue har user ko ijazat hai
        if request.method in SAFE_METHODS:
            return True
        # Create, Update, Delete ke liye check karein ge ke user ADMIN ya TEACHER ho
        return request.user.is_authenticated and request.user.role in ['ADMIN', 'TEACHER']

# ========================================================
# ATTENDANCE VIEWSET (CRUD operations with roles validation)
# ========================================================
class AttendanceViewSet(viewsets.ModelViewSet):
    serializer_class = AttendanceSerializer
    permission_classes = [IsAuthenticated, IsAdminOrTeacherOrReadOnly]

    def get_queryset(self):
        user = self.request.user
        # ⚠️ PDF Requirement: Student sirf apni attendance dekh sake, baqi sab ki nahi
        if user.role == 'STUDENT':
            return Attendance.objects.filter(student__user=user)
        # Admin aur Teacher saare students ki attendance dekh sakte hain
        return Attendance.objects.all()