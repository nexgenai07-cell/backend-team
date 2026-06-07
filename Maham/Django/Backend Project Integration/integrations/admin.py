from django.contrib import admin
from .models import UserProfile, AIRequest, Payment

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'profile_image')
    search_fields = ('name', 'email')

@admin.register(AIRequest)
class AIRequestAdmin(admin.ModelAdmin):
    list_display = ('id', 'prompt', 'created_at')
    readonly_fields = ('response', 'created_at')  # Response ko read-only rakha taake ye sirf API se hi update ho
    search_fields = ('prompt',)

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'amount', 'stripe_payment_id', 'status', 'created_at')
    readonly_fields = ('stripe_payment_id', 'status', 'created_at')  # Takay ye fields automatic Stripe handle kare
    list_filter = ('status', 'created_at')
    search_fields = ('stripe_payment_id', 'user__name')