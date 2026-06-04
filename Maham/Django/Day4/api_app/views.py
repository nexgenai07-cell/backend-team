from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Student, Teacher, Classroom, Attendance, Result, Product, Cart, Order
from .serializers import StudentSerializer, TeacherSerializer, ClassroomSerializer, AttendanceSerializer, ResultSerializer, ProductSerializer, CartSerializer, OrderSerializer
from rest_framework.generics import ListAPIView
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet


# =========================================================================
# DAY 4: STUDENT DETAIL API VIEW (Handles Task 1, 2, 3, 4, and 5)
# =========================================================================
class StudentDetailAPIView(APIView):

    # --- TASK 1 & TASK 5: Get Single Student API ---
    def get(self, request, id):
        try:
            # Database se student ko uski ID ke mutabiq dhoond rahe hain
            student = Student.objects.get(id=id)
            
            # Agar student mil jaye, to serializer use karke data ko JSON format mein badlein ge
            serializer = StudentSerializer(student)
            
            # JSON data aur 200 OK status code response mein bhej rahe hain 
            return Response(serializer.data, status=status.HTTP_200_OK)
            
        except Student.DoesNotExist:
            # TASK 5: Agar student database mein nahi milta (jaise ID 999) 
            # To proper custom error message aur 404 Not Found status code return karein ge 
            return Response({"error": "Student not found"}, status=status.HTTP_404_NOT_FOUND)


    # --- TASK 2: Update Student API Using PUT (Full Update) ---
    def put(self, request, id):
        try:
            student = Student.objects.get(id=id)
        except Student.DoesNotExist:
            return Response({"error": "Student not found"}, status=status.HTTP_404_NOT_FOUND)

        # request.data ka matlab hai jo naya data user ne bheja hai 
        # data=request.data ka matlab hai full update (saare fields lazmi bhejne honge)
        serializer = StudentSerializer(student, data=request.data)
        
        # Check kar rahe hain ke naya data validation rules ke mutabiq sahi hai ya nahi 
        if serializer.is_valid():
            serializer.save() # Data database mein save ho jayega
            # Expected output return kar rahe hain 
            return Response({"message": "Student updated successfully"}, status=status.HTTP_200_OK)
        
        # Agar validation fail ho jaye (e.g., email missing ho), to errors aur 400 Bad Request return karein ge 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    # --- TASK 3: Partial Update API Using PATCH ---
    def patch(self, request, id):
        try:
            student = Student.objects.get(id=id)
        except Student.DoesNotExist:
            return Response({"error": "Student not found"}, status=status.HTTP_404_NOT_FOUND)

        # partial=True ka matlab hai user sirf wahi fields bhej sakta hai jo change karni hain (jaise sirf age) 
        serializer = StudentSerializer(student, data=request.data, partial=True)
        
        if serializer.is_valid():
            serializer.save()
            # Expected output return kar rahe hain 
            return Response({"message": "Student partially updated"}, status=status.HTTP_200_OK)
            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    # --- TASK 4: Delete Student API ---
    def delete(self, request, id):
        try:
            student = Student.objects.get(id=id)
        except Student.DoesNotExist:
            return Response({"error": "Student not found"}, status=status.HTTP_404_NOT_FOUND)

        # Student ka record database se delete kar rahe hain
        student.delete()
        # Expected output return kar rahe hain 
        return Response({"message": "Student deleted successfully"}, status=status.HTTP_200_OK)
    
# =========================================================================
# DAY 4: STUDENT LIST, FILTER, SEARCH & ORDERING VIEW (Handles Task 6, 7, 8)
# =========================================================================
class StudentListAPIView(ListAPIView):
    # Poore students ka data database se fetch karne ke liye query
    queryset = Student.objects.all()
    
    # Validation aur conversion ke liye apna banaya hua serializer use kar rahe hain
    serializer_class = StudentSerializer
    
    # DRF ke built-in backends lagaye hain filter, search aur sort karne ke liye
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    
    # TASK 6: Kis field par filter apply karna hai (class_name ke mutabiq)
    filterset_fields = ['class_name']
    
    # TASK 7: Kis field par search chalani hai (name ke mutabiq)
    search_fields = ['name']
    
    # TASK 8: Kis field ke mutabiq data sort/order hoga (name ke mutabiq)
    ordering_fields = ['name']

# TASK 9: Teacher CRUD Views Suite
class TeacherViewSet(ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

# TASK 10: Classroom CRUD Views Suite
class ClassroomViewSet(ModelViewSet):
    queryset = Classroom.objects.all()
    serializer_class = ClassroomSerializer

# TASK 11: Student Attendance API View Set
class AttendanceViewSet(ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer

# TASK 12: Student Result API View Set
class ResultViewSet(ModelViewSet):
    queryset = Result.objects.all()
    serializer_class = ResultSerializer

# TASK 13, 14, 15: Product CRUD + Search + Filter View Set
class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    # Filtering aur Searching backends register kiye
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    
    # TASK 15: Category ke mutabiq exact filter chalane ke liye
    filterset_fields = ['category']
    
    # TASK 14: Name aur description dono mein keyword search karne ke liye
    search_fields = ['name', 'description']


# TASK 16: Cart API View Set (Handles item addition and lists)
class CartViewSet(ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer


# TASK 17: Order API View Set (Handles booking processing)
class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer