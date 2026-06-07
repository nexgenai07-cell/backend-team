import os
import logging
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from google import genai
import stripe

from .models import UserProfile, AIRequest, Payment

# Logging setup for error handling
logger = logging.getLogger(__name__)

# Stripe API key configure karein
stripe.api_key = os.getenv('STRIPE_SECRET_KEY')



@receiver(post_save, sender=UserProfile)
def send_welcome_email(sender, instance, created, **kwargs):
    """
    3. Email Integration: Automatically send a welcome email when a new user is created.
    """
    if created:
        subject = "Welcome to Our Platform!"
        message = f"Hello {instance.name},\n\nThank you for registering with us. Your account has been successfully created!"
        from_email = os.getenv('EMAIL_HOST_USER')
        recipient_list = [instance.email]
        
        try:
            send_mail(subject, message, from_email, recipient_list, fail_silently=False)
            logger.info(f"Welcome email successfully sent to {instance.email}")
        except Exception as e:
            logger.error(f"Failed to send welcome email to {instance.email}: {str(e)}")


@receiver(post_save, sender=AIRequest)
def call_gemini_api(sender, instance, created, **kwargs):
    """
    4. Gemini API Integration: Call Gemini API when a prompt is created and store the response.
    """
    if created and not instance.response:  # Ensure it runs only on creation and response is empty
        try:
            client = genai.Client(api_key=os.getenv('GEMINI_API_KEY'))
            response = client.models.generate_content(
                model='gemini-2.5-flash',  # Google ka standard modern flash model
                contents=instance.prompt,
            )
            
            # Response store karein (update fields use kar rahe hain taake infinite loop na bane)
            instance.response = response.text
            instance.save(update_fields=['response'])
            logger.info(f"Gemini response stored successfully for prompt ID {instance.id}")
        except Exception as e:
            instance.response = f"API Error: {str(e)}"
            instance.save(update_fields=['response'])
            logger.error(f"Gemini API failure for prompt ID {instance.id}: {str(e)}")


@receiver(post_save, sender=Payment)
def create_stripe_payment_intent(sender, instance, created, **kwargs):
    """
    5. Stripe Integration: Create a Payment Intent when a payment record is created.
    """
    if created and instance.status == 'PENDING':
        try:
            # Stripe ke liye amount ko cents mei convert karna hota hai (e.g., $10.00 = 1000 cents)
            amount_in_cents = int(instance.amount * 100)
            
            # Payment Intent create karein
            intent = stripe.PaymentIntent.create(
                amount=amount_in_cents,
                currency='usd',
                metadata={'user_id': instance.user.id, 'payment_id': instance.id},
                description=f"Payment for user {instance.user.name}"
            )
            
            # Database mei Stripe ID aur status update karein
            instance.stripe_payment_id = intent.id
            instance.status = 'SUCCESS' if intent.status == 'succeeded' else 'PENDING'
            instance.save(update_fields=['stripe_payment_id', 'status'])
            logger.info(f"Stripe Payment Intent {intent.id} created successfully for Payment ID {instance.id}")
            
        except stripe.error.StripeError as e:
            instance.status = 'FAILED'
            instance.stripe_payment_id = f"Stripe Error: {str(e)}"
            instance.save(update_fields=['status', 'stripe_payment_id'])
            logger.error(f"Stripe payment creation failed for Payment ID {instance.id}: {str(e)}")
        except Exception as e:
            instance.status = 'FAILED'
            instance.save(update_fields=['status'])
            logger.error(f"General error in payment processing for Payment ID {instance.id}: {str(e)}")