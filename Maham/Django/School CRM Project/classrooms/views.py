from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, BasePermission, SAFE_METHODS
from .models import Classroom
from .serializers import ClassroomSerializer

# ========================================================
# CUSTOM PERMISSION (Sirf Admin ko edit krne ki ijazat dene k liye)
# ========================================================
class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        # Agar request GET, HEAD, ya OPTIONS (SAFE_METHODS) hai to sab ko ijazat hai
        if request.method in SAFE_METHODS:
            return True
        # Create, Update, Delete ke liye check karein ge ke user login ho aur us ka role ADMIN ho
        return request.user.is_authenticated and request.user.role == 'ADMIN'

# ========================================================
# CLASSROOM VIEWSET (CRUD Operations handled automatically)
# ========================================================
class ClassroomViewSet(viewsets.ModelViewSet):
    queryset = Classroom.objects.all()
    serializer_class = ClassroomSerializer
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly] # Login hona lazmi hai