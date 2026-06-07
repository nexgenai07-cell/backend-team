from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import AIRequest
from .services import generate_response


@receiver(post_save, sender=AIRequest)
def ai_response(sender, instance, created, **kwargs):

    if created:

        try:
            instance.response = generate_response(
                instance.prompt
            )

        except Exception as e:
            instance.response = f"Gemini API Failed: {e}"

        instance.save()