import os
import stripe
from django.conf import settings
import logging

logger = logging.getLogger(__name__)

# Stripe API key initialization
stripe.api_key = getattr(settings, 'STRIPE_SECRET_KEY', os.getenv('STRIPE_SECRET_KEY'))

def create_stripe_payment_intent(amount):
    """
    Creates a Payment Intent on Stripe and returns (payment_id, status)
    """
    try:
        # Amount ko cents mein convert karna ($25.50 -> 2550)
        amount_in_cents = int(amount * 100)

        # Stripe API Call
        intent = stripe.PaymentIntent.create(
            amount=amount_in_cents,
            currency='usd',
            metadata={'integration': 'django_admin_task'}
        )
        # Agar successfully create ho jaye
        return intent.id, 'pending'
    
    except stripe.error.StripeError as e:
        logger.error(f"Stripe API Error: {str(e)}")
        return f"Stripe Error: {str(e)[:50]}", 'failed'
        
    except Exception as e:
        logger.error(f"General Stripe Service Error: {str(e)}")
        return None, 'failed'