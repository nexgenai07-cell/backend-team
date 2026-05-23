from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Student
from .serializers import StudentSerializer

# APIView banaya jo ek single student fetch karega
class StudentDetailAPIView(APIView):
    def get(self, request, pk):
        # Agar student exist nahi karta to 404 error return hoga
        student = get_object_or_404(Student, pk=pk)

        # Student object ko serializer ke through JSON me convert karna
        serializer = StudentSerializer(student)

        # Response return karna with status 200 OK
        return Response(serializer.data, status=status.HTTP_200_OK)

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Student
from .serializers import StudentSerializer

# Ye class ek API banati hai jo student ko update karegi
class StudentUpdateAPIView(APIView):
    # PUT request handle karegi (complete update)
    def put(self, request, pk):
        try:
            # Database se student record fetch karna pk ke basis par
            student = Student.objects.get(pk=pk)
        except Student.DoesNotExist:
            # Agar student exist nahi karta to 404 error return hoga
            return Response({"error": "Student not found"}, status=status.HTTP_404_NOT_FOUND)

        # Serializer ko existing student aur naye data ke sath bind karna
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            # Agar data valid hai to save karna (update record)
            serializer.save()
            # Updated student ka data return karna
            return Response(serializer.data, status=status.HTTP_200_OK)
        # Agar data invalid hai to error messages return karna
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# Ye class PATCH request handle karegi (partial update)
class StudentPartialUpdateAPIView(APIView):
    def patch(self, request, pk):
        try:
            # Database se student record fetch karna pk ke basis par
            student = Student.objects.get(pk=pk)
        except Student.DoesNotExist:
            # Agar student exist nahi karta to 404 error return hoga
            return Response({"error": "Student not found"}, status=status.HTTP_404_NOT_FOUND)

        # Serializer ko partial=True ke sath bind karna (sirf given fields update hongi)
        serializer = StudentSerializer(student, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            # Custom message return karna instead of full student data
            return Response({"message": "Student partially updated"}, status=status.HTTP_200_OK)
        # Agar data invalid hai to error messages return karna
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# Ye class DELETE request handle karegi (student record delete karegi)
class StudentDeleteAPIView(APIView):
    def delete(self, request, pk):
        try:
            # Database se student record fetch karna pk ke basis par
            student = Student.objects.get(pk=pk)
        except Student.DoesNotExist:
            # Agar student exist nahi karta to 404 error return hoga
            return Response({"error": "Student not found"}, status=status.HTTP_404_NOT_FOUND)

        # Agar student exist karta hai to delete karna
        student.delete()
        # Custom message return karna
        return Response({"message": "Student deleted successfully"}, status=status.HTTP_200_OK)
from .serializers import StudentSerializer

# Ye class GET request handle karegi (sare students list karegi)
class StudentListAPIView(APIView):
    def get(self, request):
        # Database se sare students fetch karna
        students = Student.objects.all()
        # Serializer ke through queryset ko JSON me convert karna
        serializer = StudentSerializer(students, many=True)
        # Sare students ka data return karna
        return Response(serializer.data)
from .serializers import StudentSerializer

# Ye class POST request handle karegi (naya student add karegi)
class StudentCreateAPIView(APIView):
    def post(self, request):
        # Serializer ko request data ke sath bind karna
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # Agar student successfully add ho jaye to success message return karna
            return Response({"message": "Student added successfully"}, status=status.HTTP_201_CREATED)
        # Agar data invalid ho to error return karna
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# Ye class GET request handle karegi (single student fetch karegi)
class StudentDetailAPIView(APIView):
    def get(self, request, pk):
        try:
            # Database se student record fetch karna pk ke basis par
            student = Student.objects.get(pk=pk)
        except Student.DoesNotExist:
            # Agar student exist nahi karta to error message return hoga
            return Response({"error": "Student not found"}, status=status.HTTP_404_NOT_FOUND)

        # Agar student exist karta hai to serializer ke through JSON return karna
        serializer = StudentSerializer(student)
        return Response(serializer.data, status=status.HTTP_200_OK)
class StudentByClassAPIView(APIView):
    def get(self, request):
        # Query parameter extract karo
        class_name = request.GET.get("class_name")  
        # Agar user ne ?class_name=10th diya hai to yahan "10th" milega

        #  Filter students by class_name
        if class_name:
            students = Student.objects.filter(class_name=class_name)
        else:
            students = Student.objects.all()
        # Agar param nahi diya to saare students return karenge

        #  Serialize queryset
        serializer = StudentSerializer(students, many=True)

        #  Response return karo
        return Response(serializer.data)
from django.db.models import Q   # ✅ for flexible search

class StudentSearchAPIView(APIView):
    def get(self, request):
        # Query parameter extract karo
        search_query = request.GET.get("search")

        # Agar search diya hai to filter karo
        if search_query:
            # Case-insensitive search (icontains)
            students = Student.objects.filter(
                Q(name__icontains=search_query) |
                Q(email__icontains=search_query) |
                Q(class_name__icontains=search_query)
            )
        else:
            # Agar search param nahi diya to sab students return karo
            students = Student.objects.all()

        #  Serialize queryset
        serializer = StudentSerializer(students, many=True)

        #  Response return karo
        return Response(serializer.data)
class StudentOrderAPIView(APIView):
    def get(self, request):
        # 1️⃣ Query parameter extract karo
        ordering_field = request.GET.get("ordering")

        # 2️⃣ Agar ordering param diya hai to sort karo
        if ordering_field:
            students = Student.objects.all().order_by(ordering_field)
        else:
            students = Student.objects.all()

        # 3️⃣ Serialize queryset
        serializer = StudentSerializer(students, many=True)

        # 4️⃣ Response return karo
        return Response(serializer.data)
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Teacher
from .serializers import TeacherSerializer

# Teacher CRUD APIView
class TeacherCRUDAPIView(APIView):

    # GET request: agar pk diya ho to single teacher, warna list of teachers
    def get(self, request, pk=None):
        if pk:
            try:
                teacher = Teacher.objects.get(pk=pk)   # ek teacher fetch karo
                serializer = TeacherSerializer(teacher)
                return Response(serializer.data)       # JSON return karo
            except Teacher.DoesNotExist:
                return Response({"error": "Teacher not found"}, status=status.HTTP_404_NOT_FOUND)
        else:
            teachers = Teacher.objects.all()           # saare teachers fetch karo
            serializer = TeacherSerializer(teachers, many=True)
            return Response(serializer.data)

    # POST request: naya teacher create karna
    def post(self, request):
        serializer = TeacherSerializer(data=request.data)   # request data ko serializer me pass karo
        if serializer.is_valid():                           # agar data valid hai
            serializer.save()                               # DB me save karo
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # PUT request: ek teacher ko full update karna
    def put(self, request, pk):
        try:
            teacher = Teacher.objects.get(pk=pk)            # teacher fetch karo
        except Teacher.DoesNotExist:
            return Response({"error": "Teacher not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = TeacherSerializer(teacher, data=request.data)  # full data replace karo
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)                 # updated data return karo
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # PATCH request: ek teacher ko partial update karna
    def patch(self, request, pk):
        try:
            teacher = Teacher.objects.get(pk=pk)
        except Teacher.DoesNotExist:
            return Response({"error": "Teacher not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = TeacherSerializer(teacher, data=request.data, partial=True)  # sirf kuch fields update
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # DELETE request: ek teacher ko delete karna
    def delete(self, request, pk):
        try:
            teacher = Teacher.objects.get(pk=pk)
            teacher.delete()                                # teacher record delete karo
            return Response({"message": "Teacher deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
        except Teacher.DoesNotExist:
            return Response({"error": "Teacher not found"}, status=status.HTTP_404_NOT_FOUND)
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Classroom
from .serializers import ClassroomSerializer

class ClassroomCRUDAPIView(APIView):

    # GET request: all classrooms or single classroom
    def get(self, request, pk=None):
        if pk:
            try:
                classroom = Classroom.objects.get(pk=pk)
                serializer = ClassroomSerializer(classroom)
                return Response(serializer.data)
            except Classroom.DoesNotExist:
                return Response({"error": "Classroom not found"}, status=status.HTTP_404_NOT_FOUND)
        else:
            classrooms = Classroom.objects.all()
            serializer = ClassroomSerializer(classrooms, many=True)
            return Response(serializer.data)

    # POST request: new classroom create
    def post(self, request):
        serializer = ClassroomSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # PUT request: full update
    def put(self, request, pk):
        try:
            classroom = Classroom.objects.get(pk=pk)
        except Classroom.DoesNotExist:
            return Response({"error": "Classroom not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = ClassroomSerializer(classroom, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # PATCH request: partial update
    def patch(self, request, pk):
        try:
            classroom = Classroom.objects.get(pk=pk)
        except Classroom.DoesNotExist:
            return Response({"error": "Classroom not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = ClassroomSerializer(classroom, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # DELETE request: classroom delete
    def delete(self, request, pk):
        try:
            classroom = Classroom.objects.get(pk=pk)
            classroom.delete()
            return Response({"message": "Classroom deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
        except Classroom.DoesNotExist:
            return Response({"error": "Classroom not found"}, status=status.HTTP_404_NOT_FOUND)
from .models import Attendance
from .serializers import AttendanceSerializer

class AttendanceAPIView(APIView):

    def get(self, request):
        records = Attendance.objects.all()
        serializer = AttendanceSerializer(records, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AttendanceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Result
from .serializers import ResultSerializer

class ResultAPIView(APIView):

    def get(self, request):
        results = Result.objects.all()
        serializer = ResultSerializer(results, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ResultSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from .serializers import ProductSerializer

class ProductAPIView(APIView):

    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        try:
            product = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            product = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)

        product.delete()
        return Response({"message": "Product deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
from rest_framework import generics, filters
from .models import Product
from .serializers import ProductSerializer

class ProductSearchAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'description', 'category']  # search allowed on these fields
from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Product
from .serializers import ProductSerializer

class ProductFilterAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category']   # filter allowed on category field
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Cart
from .serializers import CartSerializer

class CartAPIView(APIView):

    def get(self, request):
        carts = Cart.objects.all()
        serializer = CartSerializer(carts, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CartSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        try:
            cart = Cart.objects.get(pk=pk)
        except Cart.DoesNotExist:
            return Response({"error": "Cart item not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = CartSerializer(cart, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            cart = Cart.objects.get(pk=pk)
        except Cart.DoesNotExist:
            return Response({"error": "Cart item not found"}, status=status.HTTP_404_NOT_FOUND)

        cart.delete()
        return Response({"message": "Cart item deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
from .models import Order
from .serializers import OrderSerializer

class OrderAPIView(APIView):

    def get(self, request):
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


