from django.db import models
from .services import generate_response


class AIRequest(models.Model):
    prompt = models.TextField()
    response = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if self.prompt and not self.response:
            try:
                self.response = generate_response(self.prompt)
            except Exception as e:
                self.response = f"Gemini API Failed: {str(e)}"

        super().save(*args, **kwargs)

    def __str__(self):
        return self.prompt[:50]