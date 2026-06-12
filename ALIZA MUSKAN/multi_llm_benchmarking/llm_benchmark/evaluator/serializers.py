"""
serializers.py — Database objects ko JSON mein convert karta hai.
API response ka format yahan define hota hai.
"""

from rest_framework import serializers
from .models import EvaluationSession, ModelResponse, JudgeScore


class JudgeScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = JudgeScore
        fields = ['judge_name', 'score']


class ModelResponseSerializer(serializers.ModelSerializer):
    # Nested: har response ke saath uske scores bhi aayenge
    judge_scores = JudgeScoreSerializer(many=True, read_only=True)

    class Meta:
        model = ModelResponse
        fields = [
            'id',
            'model_name',
            'anonymous_label',
            'response_text',
            'response_time_ms',
            'final_score',
            'judge_scores',
            'created_at',
        ]


class EvaluationSessionSerializer(serializers.ModelSerializer):
    # Nested: session ke saath saare responses bhi aayenge
    responses = ModelResponseSerializer(many=True, read_only=True)

    class Meta:
        model = EvaluationSession
        fields = [
            'id',
            'prompt',
            'winner_model',
            'winner_score',
            'responses',
            'created_at',
        ]


class PromptInputSerializer(serializers.Serializer):
    """User se sirf prompt lena hai — yeh simple input serializer hai."""
    prompt = serializers.CharField(min_length=5, max_length=2000)


class LeaderboardSerializer(serializers.Serializer):
    """Leaderboard entry ka format."""
    model_name = serializers.CharField()
    total_wins = serializers.IntegerField()
    average_score = serializers.FloatField()
    total_evaluations = serializers.IntegerField()
