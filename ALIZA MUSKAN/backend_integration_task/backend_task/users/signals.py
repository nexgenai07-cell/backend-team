from django.db.models.signals import post_save
from django.dispatch import receiver

# Importing models from the local application
from .models import User, AIRequest, Payment

# Settings import to access credentials from settings.py (.env keys)
from django.conf import settings

# External HTTP library to make API requests (used for EmailJS)
import requests

# Standard python logging to keep track of backend errors
import logging

# Importing third-party service functions created for Gemini and Stripe
from .gemini_service import generate_gemini_response
from .stripeservices import create_stripe_payment_intent

# Initializing logger for this specific file
logger = logging.getLogger(__name__)

# SIGNAL 1: Welcome Email via EmailJS
@receiver(post_save, sender=User)
def send_email_via_emailjs(sender, instance, created, **kwargs):
    """
    Triggers automatically whenever a new User is created.
    Sends a welcome email using the EmailJS REST API.
    """
    # Check if a new user is created (stops this from running during user profile updates)
    if created:
        try:
            # EmailJS endpoint URL
            url = "https://api.emailjs.com/api/v1.0/email/send"

            # Constructing the payload using secure configuration keys from settings.py
            payload = {
                 "service_id": settings.EMAILJS_SERVICE_ID,
                 "template_id": settings.EMAILJS_TEMPLATE_ID,
                 "user_id": settings.EMAILJS_PUBLIC_KEY,
                 "accessToken": settings.EMAILJS_PRIVATE_KEY,
                 "template_params": {
                            "to_name": instance.name,      # Target user name from DB
                            "to_email": instance.email,    # Target user email from DB
                            }
            }

            # Debug logs to verify data payload in the terminal before sending
            print("EMAIL PAYLOAD SENT:", payload)

            # Making the synchronous POST request to EmailJS
            response = requests.post(url, json=payload)

            # Debug logs to track the API behavior
            print("EMAILJS STATUS:", response.status_code)
            print("EMAILJS RESPONSE:", response.text)

            # If response is not 200 OK, catch the custom error message
            if response.status_code != 200:
                logger.error(f"EmailJS Error: {response.text}")

        # Catching specific network issues or connection failures
        except requests.exceptions.RequestException as e:
            logger.error(f"EmailJS Request Failed: {str(e)}")

        # Catching any other unexpected system crashes
        except Exception as e:
            logger.error(f"Unexpected EmailJS Error: {str(e)}")
# SIGNAL 2: AI Response Generation via Gemini
@receiver(post_save, sender=AIRequest)
def generate_ai_response(sender, instance, created, **kwargs):
    """
    Triggers automatically when an AIRequest entry is initialized.
    Sends prompt to Gemini and updates the object with the generated response.
    """
    # Only execute on initial record creation
    if created:
        # Fetching response by sending user prompt to Gemini Service file
        response = generate_gemini_response(instance.prompt)

        # IMPORTANT: Using .update() instead of .save() to avoid Infinite Loop Recursion.
        # .update() modifies rows directly in the database without firing the post_save signal again.
        AIRequest.objects.filter(id=instance.id).update(
            response=response
        )
# SIGNAL 3: Online Payment via Stripe
@receiver(post_save, sender=Payment)
def generate_stripe_payment(sender, instance, created, **kwargs):
    """
    Triggers automatically when a Payment record is created.
    Communicates with Stripe to set up a unique checkout payment intent.
    """
    # Sirf tab chalega jab naya record create ho aur pehle se id na ho
    if created and not instance.stripe_payment_id and instance.amount > 0:
        
        # Service file se function call karna
        stripe_id, stripe_status = create_stripe_payment_intent(instance.amount)

        # Avoid recursion using .update() to bypass re-triggering post_save
        Payment.objects.filter(id=instance.id).update(
            stripe_payment_id=stripe_id,
            status=stripe_status
        )