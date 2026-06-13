from django.db import models

class Prompt(models.Model):
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text



class LLMResponse(models.Model):
    prompt = models.ForeignKey(Prompt, on_delete=models.CASCADE, related_name="responses")
    model_name = models.CharField(max_length=100)
    anonymized_label = models.CharField(max_length=10)  # e.g. A, B, C, D
    anonymized_label = models.CharField(max_length=10, default="A")

    response = models.TextField()
    response_time = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.model_name} | {self.prompt.text[:30]}"


class Evaluation(models.Model):
    response = models.ForeignKey(LLMResponse, on_delete=models.CASCADE, related_name="evaluations")
    judge_name = models.CharField(max_length=100)
    accuracy = models.FloatField()
    relevance = models.FloatField()
    completeness = models.FloatField()
    clarity = models.FloatField()
    conciseness = models.FloatField()
    total_score = models.FloatField()

    def __str__(self):
        return f"{self.judge_name} → {self.total_score}"
