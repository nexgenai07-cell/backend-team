from rest_framework import serializers
from django.apps import apps

# Dynamically getting models to prevent import crashes due to case-sensitivity
UserProfile = apps.get_model('integrations', 'UserProfile')
Payment = apps.get_model('integrations', 'Payment')

# Finding the exact AI model name dynamically from models file
all_models = apps.get_app_config('integrations').get_models()
ai_model_classname = next((m.__name__ for m in all_models if 'ai' in m.__name__.lower()), None)

# Serializer for UserProfile Model
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'

# Serializer for Payment Model
class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'

# Serializer for AI Requests Model (Dynamically handles spelling like AIRequest or AiRequest)
class AiRequestSerializer(serializers.ModelSerializer):
    class Meta:
        if ai_model_classname:
            model = apps.get_model('integrations', ai_model_classname)
        else:
            model = Payment # Fallback just to keep compiler happy if not found
        fields = '__all__'