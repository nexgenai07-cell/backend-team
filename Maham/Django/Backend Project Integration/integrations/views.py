from rest_framework.generics import ListAPIView
from django.apps import apps
from .serializers import UserProfileSerializer, PaymentSerializer, AiRequestSerializer

# Dynamically fetch models to avoid explicit casing ImportError
UserProfile = apps.get_model('integrations', 'UserProfile')
Payment = apps.get_model('integrations', 'Payment')

all_models = apps.get_app_config('integrations').get_models()
ai_model_classname = next((m.__name__ for m in all_models if 'ai' in m.__name__.lower()), None)

# API View to fetch all User Profiles
class UserProfileListAPIView(ListAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

# API View to fetch all Payments
class PaymentListAPIView(ListAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

# API View to fetch all AI Requests dynamically matching your model casing
class AiRequestListAPIView(ListAPIView):
    serializer_class = AiRequestSerializer
    
    def get_queryset(self):
        if ai_model_classname:
            TargetModel = apps.get_model('integrations', ai_model_classname)
            return TargetModel.objects.all()
        return Payment.objects.none() # Empty safe fallback if model doesn't exist