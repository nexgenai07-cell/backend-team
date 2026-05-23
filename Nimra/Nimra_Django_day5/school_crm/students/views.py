from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse

def school_info(request):
    data = {
        "school_name": "Nimra Public School",
        "address": "Sahiwal, Pakistan",
        "contact": "+92-300-1234567",
        "principal": "Mr. Asad",
        "total_students": 500,
        "total_teachers": 25
    }
    return JsonResponse(data)
from django.http import JsonResponse
from .models import Student

def student_profile(request, student_id):
    try:
        student = Student.objects.get(id=student_id)
        data = {
            "name": student.name,
            "email": student.email,
            "age": student.age,
            "class_name": student.class_name,
            "roll_no": student.roll_no,
            "is_active": student.is_active,
        }
        return JsonResponse(data)
    except Student.DoesNotExist:
        return JsonResponse({"error": "Student not found"}, status=404)
