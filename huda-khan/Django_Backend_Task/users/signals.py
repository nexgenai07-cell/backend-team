from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from .models import User


@receiver(post_save, sender=User)
def send_welcome_email(sender, instance, created, **kwargs):
    if created:
        try:
            send_mail(
                'Welcome',
                f'Hello {instance.name}, welcome!',
                'hudaakhter09@gmail.com',
                [instance.email],
                fail_silently=False,
            )
        except Exception as e:
            print(e)