from django.contrib import admin
from .models import User,AIRequest,Payment

# registered users in admin panel
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email']
@admin.register(AIRequest)
class AIRequestAdmin(admin.ModelAdmin):

    # Columns shown in admin list page
    list_display = (
    'id',
    'prompt',
    'response',
    'created_at',
)
from .models import Payment

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    # Admin list view mein ye columns show hon gy
    list_display = ('id', 'user', 'amount', 'stripe_payment_id', 'status', 'created_at')
    
    # Jab record save ho jaye toh ye fields read-only ban jayengi (unhen koi edit nahi kar sakega)
    readonly_fields = ('stripe_payment_id', 'status', 'created_at')

    def get_fields(self, request, obj=None):
        # obj=None ka matlab hai ke Naya Record ADD ho raha hai
        if obj is None:
            return ('user', 'amount') # Form par sirf ye do cheezen show hon gi
        
        # Agar purana record open kiya hai (View/Change mode), toh saari fields dikhao
        return ('user', 'amount', 'stripe_payment_id', 'status', 'created_at')