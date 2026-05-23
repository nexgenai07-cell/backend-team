from django.shortcuts import render

# Task 3 -- First API Endpoint
# Instructions:
# - Create route: /home
# - Return welcome message using JsonResponse

# Yeh line basically Django ko yeh bta rhi hai k hmein aik khaas tool chahiye jo
#  hmary data ko JSON format mein badal skay.
from django.http import JsonResponse

def home_view(request):
    return JsonResponse({"message": "Welcome to School CRM"})
# task 4

def school_info_view(request):
    # School ki details ko ek Python dictionary mein store kiya
    school_data = {
        "school_name": "NextGen AI Academy",
        "total_students": 150,
        "location": "Main Campus, Lahore",
        "established_year": 2024,
        "status": "Active"
    }
    # JsonResponse is dictionary ko khud hi JSON format mein convert kr k return kr degi
    return JsonResponse(school_data)
# task 5
def student(request):
    # School ki details ko ek Python dictionary mein store kiya
    student_data = {
            "name": "Ali",
            "class": "10th",
            "roll_no": 25
    }
    # JsonResponse is dictionary ko khud hi JSON format mein convert kr k return kr degi
    return JsonResponse(student_data)
def multiple_students_view(request):
    # Students ka data aik list ke andar dictionaries ki shakal mein hai
    students_list = [
        {
            "name": "Ali",
            "class": "10th"
        },
        {
            "name": "Sara",
            "class": "9th"
        }
    ]
    # safe=False lagana zaroori hai kyunki hum top-level pr dictionary nahi, balkay List bhej rhy hain
    return JsonResponse(students_list, safe=False)

# Task 7: Real Dynamic Student View with Multiple Data
def dynamic_student_view(request, student_id):
    # Humne ek fake database (dictionary) bana li jis mein 3 students ka data hai
    students_database = {
        1: {"name": "Ali", "class": "10th", "roll_no": 25},
        2: {"name": "Sara", "class": "9th", "roll_no": 12},
        3: {"name": "Hamza", "class": "11th", "roll_no": 45}
    }
    
    # Check krein gy ke jo ID user ne mangi hai, kya woh hmare paas hai?
    if student_id in students_database:
        # Agar ID mil gayi, to us student ka data nikalrein gy
        student_info = students_database[student_id]
        
        # Output generate krein gy jesa task mein manga tha
        response_data = {
            "student_id": student_id,
            "name": student_info["name"],
            "class": student_info["class"],    
        }
        return JsonResponse(response_data)
    else:
        # Agar ID database mein nahi hai (e.g. kisi ne /student/5/ likh diya)
        return JsonResponse({"error": f"Student with ID {student_id} not found"}, status=404)
    
# task 8
def classroom(request):
    # School ki details ko ek Python dictionary mein store kiya
     class_data = {
        "class_name": "10th",
        "teacher": "Ahmed",
        "students": 40
    }
    # JsonRes ponse is dictionary ko khud hi JSON format mein convert kr k return kr degi
     return JsonResponse(class_data)
# task 9
def attendance_view(request):
    # Attendance ka status dictionary mein store kiya jesa expected output mein manga hai
    attendance_data = {
        "student": "Ali",
        "status": "Present"
    }
    # Dictionary ko JSON format mein return kr rhy hain
    return JsonResponse(attendance_data)

# Task 10: Nested School and Students Data View
def nested_school_view(request):
    # Nested dictionary structure jesa expected output mein manga gaya hai
    school_nested_data = {
        "school": "ABC School",
        "students": [
            {
                "name": "Ali",
                "marks": 85
            },
            {
                "name": "Sara",
                "marks": 90
            }
        ]
    }
    # Top-level pr dictionary hai, is liye yeh direct JSON mein convert ho jaye gi
    return JsonResponse(school_nested_data)
# task 11/
def about_view(request):
    # Project ki details ko dictionary mein store kiya jesa expected output mein manga hai
    about_data = {
        "project": "School CRM",
        "module": "Django Basics"
    }
    # Dictionary ko JSON format mein return kr rhy hain
    return JsonResponse(about_data)
# Task 12: Result Check View
def result_view(request, marks):
    # Marks ko integer mein convert kr rhy hain (taakay arithmetic check ho sakay)
    marks = int(marks)
    
    # If-Else logic status check krne k liye
    if marks >= 50:
        status = "Pass"
    else:
        status = "Fail"
        
    # Final response dictionary structure
    response_data = {
        "marks": marks,
        "result": status
    }
    
    return JsonResponse(response_data)
# Task 13: Mini School Dashboard View
def dashboard_view(request):
    # Dashboard ki statistics ko dictionary mein store kiya jesa expected output mein manga hai
    dashboard_stats = {
        "total_students": 500,
        "total_teachers": 20,
        "total_classes": 15
    }
    # Dictionary ko JSON format mein return kr rhy hain
    return JsonResponse(dashboard_stats)