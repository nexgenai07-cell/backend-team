from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
def home(request):
                    return JsonResponse({'message': 'Welcome to the Student Management System API'})
def school_info(request):      
   return JsonResponse({
        "school_name": "ABC School",
        "city": "Lahore",
        "total_students": 500
    })
def student_profile(request):
        return JsonResponse({
                    "name": "John Doe",
                    "roll_number": "12345",
                    "grade": "10th",

        })
def student_detail(request,id):
        students = {
        1: {"name": "Ali Khan", "roll_number": "101", "class": "10th Grade"},
        2: {"name": "Sara Ahmed", "roll_number": "102", "class": "9th Grade"},
        3: {"name": "Bilal Hussain", "roll_number": "103", "class": "8th Grade"},
    }
        student=students.get(id,{"error": "Student not found"})
        return JsonResponse(student)
def attandance(request):
        return JsonResponse({
                "status":"present"
        })
def result(request, marks):
    if marks >= 50:
        status = "Pass"
    else:
        status = "Fail"
    return JsonResponse({"marks": marks, "result": status})
def multiple_students(request):
    students = [
        {"name": "Ali", "class": "10th"},
        {"name": "Sara", "class": "9th"},
        {"name": "Bilal", "class": "8th"}
    ]
    return JsonResponse(students, safe=False)
def classroom(request):
    return JsonResponse({
        "class_name": "10th",
        "teacher": "Ahmed",
        "students": 40
    })
def nested_school(request):
    return JsonResponse({
        "school": "ABC School",
        "students": [
            {"name": "Ali", "marks": 85},
            {"name": "Sara", "marks": 90}
        ]
    })
def about(request):
    return JsonResponse({
        "project": "School CRM",
        "module": "Django Basics"
    })
def dashboard(request):
    return JsonResponse({
        "total_students": 500,
        "total_teachers": 20,
        "total_classes": 15
    })

