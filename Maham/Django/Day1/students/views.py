from django.http import JsonResponse

# Task 3: First API Endpoint (/home)
def home_view(request):
    return JsonResponse({"message": "Welcome to School CRM"})

# Task 4: School Information API (/school-info)
def school_info_view(request):
    data = {
        "school_name": "ABC School",
        "city": "Lahore",
        "total_students": 500
    }
    return JsonResponse(data)

# Task 5: Student Profile API (/student)
def student_profile_view(request):
    data = {
        "name": "Ali",
        "class": "10th",
        "roll_no": 25
    }
    return JsonResponse(data)

# Task 6: Multiple Students API (/students-list)
def multiple_students_view(request):
    data = [
        {"name": "Ali", "class": "10th"},
        {"name": "Sara", "class": "9th"}
    ]
    return JsonResponse(data, safe=False) # List return karne k liye safe=False zaroori hai

# Task 7: Dynamic URL (/student/<id>)
def dynamic_student_view(request, id):
    data = {
        "student_id": id,
        "name": "Ali"
    }
    return JsonResponse(data)

# Task 8: Class Details API (/classroom)
def classroom_view(request):
    data = {
        "class_name": "10th",
        "teacher": "Ahmed",
        "students": 40
    }
    return JsonResponse(data)

# Task 9: Attendance API (/attendance)
def attendance_view(request):
    data = {
        "student": "Ali",
        "status": "Present"
    }
    return JsonResponse(data)

# Task 10: Nested JSON Response (/nested-school)
def nested_school_view(request):
    data = {
        "school": "ABC School",
        "students": [
            {"name": "Ali", "marks": 85},
            {"name": "Sara", "marks": 90}
        ]
    }
    return JsonResponse(data)

# Task 11: About Route (/about)
def about_view(request):
    data = {
        "project": "School CRM",
        "module": "Django Basics"
    }
    return JsonResponse(data)

# Task 12: Result API (/result/<marks>)
def result_view(request, marks):
    # Conditionally check mapping logic
    result_status = "Pass" if marks >= 50 else "Fail"
    data = {
        "marks": marks,
        "result": result_status
    }
    return JsonResponse(data)

# Task 13: Mini School Dashboard API (/dashboard)
def dashboard_view(request):
    data = {
        "total_students": 500,
        "total_teachers": 20,
        "total_classes": 15
    }
    return JsonResponse(data)