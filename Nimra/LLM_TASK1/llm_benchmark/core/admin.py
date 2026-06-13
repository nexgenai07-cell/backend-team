from django.contrib import admin
from .models import Prompt, LLMResponse, Evaluation

@admin.register(Prompt)
class PromptAdmin(admin.ModelAdmin):
    list_display = ("id", "text", "created_at")
    search_fields = ("text",)


@admin.register(LLMResponse)
class LLMResponseAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "prompt",
        "model_name",
        "anonymized_label",
        "short_response",
        "response_time",
        "created_at",
    )
    list_filter = ("model_name", "created_at")
    search_fields = ("model_name", "response")

    def short_response(self, obj):
        return obj.response[:100] + "..." if len(obj.response) > 100 else obj.response
    short_response.short_description = "Response"


@admin.register(Evaluation)
class EvaluationAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "response",
        "judge_name",
        "accuracy",
        "relevance",
        "completeness",
        "clarity",
        "conciseness",
        "total_score",
    )
    list_filter = ("judge_name",)
    search_fields = ("judge_name", "response__model_name")
