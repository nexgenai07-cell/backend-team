from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework_simplejwt.tokens import RefreshToken

from .serializer import RegisterSerializer
from .models import CustomUser


# Registration APIView
class RegisterAPIView(APIView):# APIView → DRF ka base class hai jisme tum apne custom methods (get, post, etc.) define karti ho.
#Yahan hum ek registration API bana rahe hain jo POST request handle karega.
    def post(self, request):# POST method ko handle karta hai. Jab user registration form submit karega, toh ye method call hoga.
        serializer = RegisterSerializer(data=request.data) # Serializer ko request data ke saath initialize karta hai. Serializer data ko validate aur save karne ke liye use hota hai.
        if serializer.is_valid():# Serializer ke is_valid() method ko call karta hai jo data ko validate karta hai. Agar data valid hai, toh ye True return karega.
            serializer.save()# Serializer ke save() method ko call karta hai jo validated data ko database mein save karta hai. Yahan pe humne RegisterSerializer mein create() method define kiya hai jo CustomUser model ka instance create karta hai.
            return Response({"message": "User registered successfully"}, status=status.HTTP_201_CREATED)# Agar registration successful hai, toh ek success message ke saath HTTP 201 Created status return karta hai.
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Login APIView
class LoginAPIView(APIView):# Login APIView bhi APIView class se inherit karta hai aur POST method ko handle karta hai. Jab user login form submit karega, toh ye method call hoga.
    def post(self, request):
        username = request.data.get("username")# Request data se username aur password ko extract karta hai. request.data ek dictionary hota hai jisme user ke input data hota hai.
        password = request.data.get("password")

        user = authenticate(username=username, password=password)# Django ka built-in authenticate function ko call karta hai jo username aur password ko verify karta hai. Agar credentials valid hain, toh ye user object return karega; agar invalid hain, toh None return karega.

        if user is not None:# Agar user object valid hai (yaani credentials sahi hain), toh JWT token generate karta hai. RefreshToken.for_user(user) method ko call karta hai jo user ke liye ek refresh token create karta hai. Access token ko refresh token se access_token attribute ke through access kiya jata hai.
            refresh = RefreshToken.for_user(user)
            return Response({
                "access": str(refresh.access_token),
                "refresh": str(refresh)
            }, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Invalid username or password"}, status=status.HTTP_401_UNAUTHORIZED)


# Profile APIView
class ProfileAPIView(APIView): # ProfileAPIView bhi APIView class se inherit karta hai aur GET method ko handle karta hai. Jab user apni profile dekhna chahega, toh ye method call hoga.
    permission_classes = [IsAuthenticated] # IsAuthenticated permission class ko set karta hai, jiska matlab hai ki sirf authenticated users hi is API ko access kar sakte hain. Agar koi unauthenticated user is API ko access karne ki koshish karega, toh unhe HTTP 401 Unauthorized error milega.

    def get(self, request):
        user = request.user
        return Response({
            "username": user.username,
            "email": user.email,
            "role": user.role if hasattr(user, 'role') else "user"
        }, status=status.HTTP_200_OK)

# Student Registration
class StudentRegisterAPIView(APIView):
    def post(self, request):
        username = request.data.get("username")
        email = request.data.get("email")
        password = request.data.get("password")

        if CustomUser.objects.filter(username=username).exists():
            return Response({"error": "Username already exists"}, status=status.HTTP_400_BAD_REQUEST)

        user = CustomUser.objects.create_user(
            username=username,
            email=email,
            password=password,
            role='student'
        )
        return Response({"message": "Student registered successfully"}, status=status.HTTP_201_CREATED)


# Student Profile
class StudentProfileAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        return Response({
            "username": user.username,
            "email": user.email,
            "role": user.role
        }, status=status.HTTP_200_OK)

# Teacher Registration
class TeacherRegisterAPIView(APIView):
    def post(self, request):
        username = request.data.get("username")
        email = request.data.get("email")
        password = request.data.get("password")

        if CustomUser.objects.filter(username=username).exists():
            return Response({"error": "Username already exists"}, status=status.HTTP_400_BAD_REQUEST)

        user = CustomUser.objects.create_user( # create_user method ko call karta hai jo CustomUser model ka instance create karta hai. Yahan pe hum role ko 'teacher' set kar rahe hain.
            username=username,
            email=email,
            password=password,
            role='teacher'
        )
        return Response({"message": "Teacher registered successfully"}, status=status.HTTP_201_CREATED)


# Teacher Dashboard
class TeacherDashboardAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        return Response({
            "username": user.username,
            "email": user.email,
            "role": user.role,
            "message": f"Welcome {user.username}, this is your teacher dashboard."
        }, status=status.HTTP_200_OK)

# Admin Dashboard
class AdminDashboardAPIView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        return Response({"message": "Welcome Admin!"}, status=status.HTTP_200_OK)

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import Cart, Order
from .serializer import CartSerializer, OrderSerializer

# ---------------- CART SYSTEM ----------------
# Authenticated customer cart mein item add kar sakta hai.
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_to_cart(request):
    serializer = CartSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user)
        return Response({"message": "Item added to cart"}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def view_cart(request):
    cart_items = Cart.objects.filter(user=request.user)
    serializer = CartSerializer(cart_items, many=True)
    return Response(serializer.data)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def remove_from_cart(request, pk):
    try:
        item = Cart.objects.get(pk=pk, user=request.user)
        item.delete()
        return Response({"message": "Item removed from cart"}, status=status.HTTP_200_OK)
    except Cart.DoesNotExist:
        return Response({"error": "Item not found"}, status=status.HTTP_404_NOT_FOUND)

# ---------------- ORDER SYSTEM ----------------
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def place_order(request):
    serializer = OrderSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user)
        return Response({"message": "Order placed successfully"}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def view_orders(request):
    orders = Order.objects.filter(user=request.user)
    serializer = OrderSerializer(orders, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def admin_view_orders(request):
    if request.user.role == 'admin':
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)
    return Response({"error": "Not authorized"}, status=status.HTTP_403_FORBIDDEN)
from rest_framework_simplejwt.tokens import RefreshToken

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout_view(request):
    try:
        refresh_token = request.data["refresh"]
        token = RefreshToken(refresh_token)
        token.blacklist()
        return Response({"message": "Logout successful"}, status=status.HTTP_205_RESET_CONTENT)
    except Exception as e:
        return Response({"error": "Invalid token"}, status=status.HTTP_400_BAD_REQUEST)

class ChangePasswordAPIView(APIView):
    permission_classes = [IsAuthenticated]  # Sirf logged-in users hi access kar sakte hain

    def post(self, request):
        user = request.user  # Current logged-in user ko fetch karo
        old_password = request.data.get("old_password")  # Input se old password lo
        new_password = request.data.get("new_password")  # Input se new password lo

        # Step 1: Old password verify karo
        if not user.check_password(old_password):
            return Response({"error": "Old password is incorrect"}, status=status.HTTP_400_BAD_REQUEST)

        # Step 2: Agar old password sahi hai → new password set karo
        user.set_password(new_password)  # Securely hash karke new password set karega
        user.save()  # Database mein save karo

        # Step 3: Success response bhejo
        return Response({"message": "Password updated successfully"}, status=status.HTTP_200_OK)
class UpdateProfileAPIView(APIView):
    permission_classes = [IsAuthenticated]  # Sirf logged-in users hi apna profile update kar sakte hain

    def put(self, request):
        user = request.user  # Current logged-in user ko fetch karo

        # Step 1: Input se fields lo aur update karo
        user.username = request.data.get("username", user.username)
        user.email = request.data.get("email", user.email)
        user.phone = request.data.get("phone", user.phone)
        user.address = request.data.get("address", user.address)

        # Step 2: Save changes in database
        user.save()

        # Step 3: Success response bhejo
        return Response({"message": "Profile updated successfully"}, status=status.HTTP_200_OK)
# views.py
class CustomerRegisterAPIView(APIView):
    def post(self, request):
        user = CustomUser.objects.create_user(
            username=request.data["username"],
            email=request.data["email"],
            password=request.data["password"],
            role="customer"
        )
        return Response({"message": "Customer registered successfully"}, status=status.HTTP_201_CREATED)

class CustomerProfileAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({
            "username": request.user.username,
            "email": request.user.email,
            "role": request.user.role
        })

class CustomerUpdateProfileAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request):
        user = request.user
        user.email = request.data.get("email", user.email)
        user.phone = request.data.get("phone", user.phone)
        user.address = request.data.get("address", user.address)
        user.save()
        return Response({"message": "Customer profile updated successfully"})
class SellerRegisterAPIView(APIView):
    def post(self, request):
        user = CustomUser.objects.create_user(
            username=request.data["username"],
            email=request.data["email"],
            password=request.data["password"],
            role="seller",
            shop_name=request.data.get("shop_name", "")
        )
        return Response({"message": "Seller registered successfully"}, status=status.HTTP_201_CREATED)

class SellerDashboardAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        if request.user.role != "seller":
            return Response({"error": "Only sellers can access dashboard"}, status=status.HTTP_403_FORBIDDEN)
        return Response({
            "username": request.user.username,
            "shop_name": request.user.shop_name,
            "message": f"Welcome {request.user.username}, manage your products here."
        })
from .models import Product
from .serializer import ProductSerializer

class ProductAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):  # Add product
        if request.user.role != "seller":
            return Response({"error": "Only sellers can add products"}, status=status.HTTP_403_FORBIDDEN)
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(seller=request.user)
            return Response({"message": "Product added"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):  # Update product
        try:
            product = Product.objects.get(pk=pk, seller=request.user)
        except Product.DoesNotExist:
            return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = ProductSerializer(product, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Product updated"})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):  # Delete product
        try:
            product = Product.objects.get(pk=pk, seller=request.user)
            product.delete()
            return Response({"message": "Product deleted"})
        except Product.DoesNotExist:
            return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)

    def get(self, request):  # Customers can view products
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
