from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Student
from .serializers import StudentSerializer
from .models import Teacher
from .serializers import TeacherSerializer
from .models import Class
from .serializers import ClassSerializer

# Task 4 & Task 6: Student List APIView
class StudentListAPIView(APIView):
    
    # GET request handler: Tamam students ka data dikhane ke liye
    def get(self, request):
        students = Student.objects.all()  # Database se sab records nikale
        serializer = StudentSerializer(students, many=True)  # JSON mei convert kiya (many=True kyun ke multiple students hain)
        return Response(serializer.data, status=status.HTTP_200_OK)  # Proper status code 200 OK ke sath response bheja
        # POST request handler: Naya student create karne ke liye
    def post(self, request):
        serializer = StudentSerializer(data=request.data) # Front-end se aya data serializer ko diya
        
        if serializer.is_valid(): # Agar data bilkul theek hai (Validation pass)
            serializer.save() # Database mei save kar diya
            return Response(
                {"message": "Student created successfully"}, 
                status=status.HTTP_201_CREATED # Task 9: Proper 201 Status Code
            )
        
        # Task 8 & 9: Agar data kharab ho to errors aur 400 Status Code return karein
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# Task 7: Teacher API Implementation using APIView
class TeacherListAPIView(APIView):
    
    # GET: Tamam teachers ka data return karne ke liye
    def get(self, request):
        teachers = Teacher.objects.all()
        serializer = TeacherSerializer(teachers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # POST: Naya teacher register/save karne ke liye
    def post(self, request):
        serializer = TeacherSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Teacher created successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# Task 10 & 11: Single Student Detail APIView
class StudentDetailAPIView(APIView):
    
    # Kisi specific ID wale student ka data get karne ke liye
    def get(self, request, id):
        try:
            student = Student.objects.get(id=id) # Database se ID ke zariye student dhoonda
            serializer = StudentSerializer(student)
            return Response(serializer.data, status=status.HTTP_200_OK) # Task 9: 200 OK
        except Student.DoesNotExist:
            # Task 11: Agar ID valid na ho to custom error aur 404 Status Code return karein
            return Response({"error": "Student not found"}, status=status.HTTP_404_NOT_FOUND)
        
# Task 12 & 13: Class API View for GET and POST
class ClassListAPIView(APIView):
    
    # GET: Tamam classes ki list dekhne ke liye
    def get(self, request):
        classes = Class.objects.all()
        serializer = ClassSerializer(classes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # POST: Nayi class add karne ke liye
    def post(self, request):
        serializer = ClassSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Class created successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)