from django.urls import path
from .views import StudentDetailAPIView
from .views import StudentUpdateAPIView,StudentPartialUpdateAPIView, StudentDeleteAPIView, StudentListAPIView,StudentCreateAPIView,StudentByClassAPIView
from .views import StudentSearchAPIView,StudentOrderAPIView,TeacherCRUDAPIView,ClassroomCRUDAPIView, AttendanceAPIView,ResultAPIView,ProductSearchAPIView,ProductAPIView,ProductFilterAPIView,CartAPIView
# URL banaya jo pk ke basis par student fetch karega
from .views import (

    ProductAPIView, CartAPIView, OrderAPIView
)

urlpatterns = [

    path('student/<int:pk>/', StudentDetailAPIView.as_view()),
    # Update student ke liye URL banaya
    path('student/update/<int:pk>/', StudentUpdateAPIView.as_view()),
    # Partial update student ke liye URL banaya
    path('student/partial-update/<int:pk>/', StudentPartialUpdateAPIView.as_view()),
     # Delete student ke liye URL banaya
    path('student/delete/<int:pk>/', StudentDeleteAPIView.as_view()),
    # List all students ke liye URL banaya
    path('student/list/', StudentListAPIView.as_view()),
    path('student/add/', StudentCreateAPIView.as_view()),
      # Single student fetch ke liye URL banaya
    path('student/<int:pk>/', StudentDetailAPIView.as_view()),
    path("", StudentByClassAPIView.as_view()),
    path("", StudentSearchAPIView.as_view()),  # ✅ /students/?search=ali
    path("", StudentOrderAPIView.as_view()),  # ✅ /students/?ordering=name
    path('teachers/', TeacherCRUDAPIView.as_view()),          # GET all, POST
    path('teachers/<int:pk>/', TeacherCRUDAPIView.as_view()), # GET one, PUT, PATCH, DELETE
    path('classrooms/', ClassroomCRUDAPIView.as_view()),          # GET all, POST
    path('classrooms/<int:pk>/', ClassroomCRUDAPIView.as_view()), # GET one, PUT, PATCH, DELET
    path('attendance/', AttendanceAPIView.as_view()),
    path('results/', ResultAPIView.as_view()),
    path('products/', ProductAPIView.as_view()),          # GET, POST
    path('products/<int:pk>/', ProductAPIView.as_view()), # PUT, DELETE
    path('products/', ProductSearchAPIView.as_view()),  # GET with search
    path('products/', ProductFilterAPIView.as_view()),  # GET with filter
     path('cart/', CartAPIView.as_view()),          # GET, POST
    path('cart/<int:pk>/', CartAPIView.as_view()), # PUT, DELETE
    path('products/', ProductAPIView.as_view()),
    path('cart/', CartAPIView.as_view()),
    path('orders/', OrderAPIView.as_view()),
]






# <int:pk> ek path converter hai jo URL se integer value capture karta hai.

# Ye value view function me pk parameter ke through milti hai.

# Isse tum dynamic URLs bana sakti ho jisme har student apne unique ID se access hota hai.
# URL for POST → http://127.0.0.1:8000/students/teachers/
# http://127.0.0.1:8000/students/teachers/