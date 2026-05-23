from django.http import JsonResponse

def home(request):
    return JsonResponse({
        "message": "Welcome to School CRM"
    })


def school_info(request):
    return JsonResponse({
        "school_name": "ABC School",
        "city": "Lahore",
        "students": 500
    })


def student_profile(request):
    return JsonResponse({
        "name": "Ali",
        "class": "10th",
        "roll_no": 25
    })
    
def multiple_students(request):
    students = [
        {"name": "Ali", "class": "10th"},
        {"name": "Sara", "class": "9th"}
    ]

    return JsonResponse(students, safe=False)

def student_detail(request, id):
    return JsonResponse({
        "student_id": id,
        "name": "Ali"
    })
    
def result(request, marks):
    if marks >= 50:
        res = "Pass"
    else:
        res = "Fail"

    return JsonResponse({
        "marks": marks,
        "result": res
    })
    
def dashboard(request):
    return JsonResponse({
        "total_students": 500,
        "total_teachers": 20,
        "total_classes": 15
    })