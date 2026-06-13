"""
admin.py — Admin panel full configuration.

EvaluationSession ke andar:
  - Saare ModelResponses inline dikhte hain
  - Har ModelResponse ke andar JudgeScores bhi dikhte hain
"""

from django.contrib import admin
from django.utils.html import format_html
from .models import EvaluationSession, ModelResponse, JudgeScore


# ─────────────────────────────────────────────
# JudgeScore — ModelResponse ke andar inline
# ─────────────────────────────────────────────
class JudgeScoreInline(admin.TabularInline):
    """
    ModelResponse detail page pe judge scores
    seedha neeche table mein dikhenge.
    """
    model = JudgeScore
    extra = 0                          # empty extra rows mat dikhao
    readonly_fields = ['judge_name', 'score', 'created_at']
    can_delete = False


# ─────────────────────────────────────────────
# ModelResponse — Session ke andar inline
# ─────────────────────────────────────────────
class ModelResponseInline(admin.StackedInline):
    """
    EvaluationSession detail page pe saare model
    responses expand hokar dikhenge.
    """
    model = ModelResponse
    extra = 0
    readonly_fields = [
        'model_name', 'anonymous_label', 'response_text',
        'response_time_ms',  'created_at'
    ]
    can_delete = False
    show_change_link = True            # response pe click karke detail bhi dekh sakte hain


# ─────────────────────────────────────────────
# EvaluationSession Admin
# ─────────────────────────────────────────────
@admin.register(EvaluationSession)
class EvaluationSessionAdmin(admin.ModelAdmin):
    """
    Main session list — yahan saare prompts aur winners dikhte hain.
    """

    # List page pe yeh columns dikhenge
    list_display = [
        'id',
        'short_prompt',       # custom method — long prompt cut karta hai
        'winner_model',
        'colored_score',      # custom method — score ko color se dikhata hai
        'total_responses',    # custom method — kitne models ne jawab diya
        'created_at',
    ]

    # Right side filter panel
    list_filter = ['winner_model', 'created_at']

    # Search bar — prompt aur winner se search hoga
    search_fields = ['prompt', 'winner_model']

    # Newest first
    ordering = ['-created_at']

    # Detail page pe responses bhi dikhenge (inline)
    inlines = [ModelResponseInline]

    # Yeh fields sirf read-only honge detail page pe
    readonly_fields = ['created_at', 'winner_model', 'winner_score']

    # ── Custom display methods ──

    def short_prompt(self, obj):
        """Prompt ke pehle 60 characters dikhao."""
        return obj.prompt[:60] + '...' if len(obj.prompt) > 60 else obj.prompt
    short_prompt.short_description = 'Prompt'

    def colored_score(self, obj):
        """Score ko color ke saath dikhao — green agar high, red agar low."""
        if obj.winner_score is None:
            return '—'
        score = obj.winner_score
        if score >= 8:
            color = 'green'
        elif score >= 6:
            color = 'orange'
        else:
            color = 'red'
        return format_html(
            '<b style="color: {};">{}</b>', color, round(score, 2)
        )
    colored_score.short_description = 'Winner Score'

    def total_responses(self, obj):
        """Kitne models ne is session mein jawab diya."""
        return obj.responses.count()
    total_responses.short_description = 'Models Used'


# ─────────────────────────────────────────────
# ModelResponse Admin
# ─────────────────────────────────────────────
@admin.register(ModelResponse)
class ModelResponseAdmin(admin.ModelAdmin):
    """
    Har model response ki apni detail page.
    """

    list_display = [
        'id',
        'model_name',
        'anonymous_label',
        'session_id_link',     # custom — session ID dikhao
        'colored_final_score',
        'response_time_display',
        'created_at',
    ]

    list_filter = ['model_name', 'created_at']
    search_fields = ['model_name', 'response_text']
    ordering = ['-created_at']
    readonly_fields = [
        'session', 'model_name', 'anonymous_label',
        'response_text', 'response_time_ms',  'created_at'
    ]

    # Judge scores neeche dikhenge
    inlines = [JudgeScoreInline]

    def session_id_link(self, obj):
        return f"Session #{obj.session.id}"
    session_id_link.short_description = 'Session'

    def colored_final_score(self, obj):
        if obj.final_score is None:
            return '—'
        score = obj.final_score
        color = 'green' if score >= 8 else ('orange' if score >= 6 else 'red')
        return format_html('<b style="color: {};">{}</b>', color, round(score, 2))
    colored_final_score.short_description = 'Final Score'

    def response_time_display(self, obj):
        """ms ko readable format mein dikhao."""
        ms = obj.response_time_ms
        if ms >= 1000:
            return f"{round(ms/1000, 2)} sec"
        return f"{round(ms)} ms"
    response_time_display.short_description = 'Response Time'


# ─────────────────────────────────────────────
# JudgeScore Admin
# ─────────────────────────────────────────────
@admin.register(JudgeScore)
class JudgeScoreAdmin(admin.ModelAdmin):
    """
    Har judge ka score alag dekh sakte hain.
    """

    list_display = [
        'id',
        'judge_name',
        'score',
        'response_model_name',   # kis model ko score diya
        'response_label',        # label (A/B/C)
        'created_at',
    ]

    list_filter = ['judge_name', 'created_at']
    search_fields = ['judge_name']
    ordering = ['-created_at']
    readonly_fields = ['judge_name', 'score', 'model_response', 'created_at']

    def response_model_name(self, obj):
        return obj.model_response.model_name
    response_model_name.short_description = 'Model'

    def response_label(self, obj):
        return obj.model_response.anonymous_label
    response_label.short_description = 'Label'