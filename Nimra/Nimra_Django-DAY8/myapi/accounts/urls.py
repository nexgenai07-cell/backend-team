from django.urls import path
from .views import  LoginAPIView, ProfileAPIView
from .views import TeacherRegisterAPIView, TeacherDashboardAPIView,RegisterAPIView
from .views import AdminDashboardAPIView, StudentRegisterAPIView, StudentProfileAPIView,add_to_cart, view_cart, remove_from_cart, place_order, view_orders, admin_view_orders,logout_view, ChangePasswordAPIView, UpdateProfileAPIView, CustomerRegisterAPIView, CustomerProfileAPIView, CustomerUpdateProfileAPIView
from .views import SellerRegisterAPIView, SellerDashboardAPIView, ProductAPIView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView



urlpatterns = [
    # Registration endpoints
    path('register/', RegisterAPIView.as_view(), name='register'),
    path('student/register/', StudentRegisterAPIView.as_view(), name='student_register'),
    path('teacher/register/', TeacherRegisterAPIView.as_view(), name='teacher_register'),
    
    # Login/Authentication endpoints
    path('login/', LoginAPIView.as_view(), name='login'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    # Profile endpoints
    path('profile/', ProfileAPIView.as_view(), name='profile'),
    path('student/profile/', StudentProfileAPIView.as_view(), name='student_profile'),
    
    # Dashboard endpoints
    path('teacher/dashboard/', TeacherDashboardAPIView.as_view(), name='teacher_dashboard'),
    path('admin/dashboard/', AdminDashboardAPIView.as_view(), name='admin_dashboard'),
    # Cart
    path('cart/add/', add_to_cart),
    path('cart/view/', view_cart),
    path('cart/remove/<int:pk>/', remove_from_cart),

    # Orders
    path('order/place/', place_order),
    path('order/view/', view_orders),
    path('order/admin/', admin_view_orders),

    # Logout
    path('logout/', logout_view),
     path('change-password/', ChangePasswordAPIView.as_view(), name='change_password'),
      path('update-profile/', UpdateProfileAPIView.as_view(), name='update_profile'),
      # Customer endpoints
    path('customer/register/', CustomerRegisterAPIView.as_view(), name='customer_register'),
    path('customer/profile/', CustomerProfileAPIView.as_view(), name='customer_profile'),
    path('customer/update-profile/', CustomerUpdateProfileAPIView.as_view(), name='customer_update_profile'),

    # Seller endpoints
    path('seller/register/', SellerRegisterAPIView.as_view(), name='seller_register'),
    path('seller/dashboard/', SellerDashboardAPIView.as_view(), name='seller_dashboard'),

    # Product endpoints
    path('products/', ProductAPIView.as_view(), name='product_list_create'),   # GET (view all), POST (add product)
    path('products/<int:pk>/', ProductAPIView.as_view(), name='product_update_delete'),  # PUT, DELETE
]


