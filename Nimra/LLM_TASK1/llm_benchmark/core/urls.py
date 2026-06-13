from django.urls import path
from core.views import submit_prompt_openrouter

urlpatterns = [
    path("submit_prompt_openrouter/", submit_prompt_openrouter, name="submit_prompt_openrouter"),
]
