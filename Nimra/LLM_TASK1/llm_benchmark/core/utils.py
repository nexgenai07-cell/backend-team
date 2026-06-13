import requests
import os
import time
from django.conf import settings
from .models import LLMResponse

BASE_URL = "https://openrouter.ai/api/v1/chat/completions"
API_KEY = settings.OPENROUTER_API_KEY

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

def ask_model(model, question):
    start = time.time()
    data = {
        "model": model,
        "messages": [{"role": "user", "content": question}],
        "max_tokens": 500   # ✅ free quota ke andar rakha
    }
    response = requests.post(BASE_URL, headers=headers, json=data)
    result = response.json()
    end = time.time()

    # ✅ Error handling
    if "choices" not in result:
        error_msg = result.get("error", {}).get("message", "Unknown error")
        LLMResponse.objects.create(
            model_name=model,
            prompt=question,
            response=f"Error: {error_msg}",
            response_time=end - start
        )
        return f"Error from {model}: {error_msg}"

    # ✅ Normal case
    answer = result["choices"][0]["message"]["content"]

    # Save response in DB
    LLMResponse.objects.create(
        model_name=model,
        prompt=question,
        response=answer,
        response_time=end - start
    )
    return answer

# 🔹 Models list (4 working free models)
ai_models = [
    "openai/gpt-4",                     # ✅ free quota with max_tokens fix
    "deepseek/deepseek-chat",           # ✅ free model
    "anthropic/claude-3-haiku",         # ✅ free model
    "meta-llama/llama-3-8b-instruct"  # ✅ alternate free model (instead of mistral)
]

# Judges list (2 reliable models)
judges = ["deepseek/deepseek-chat", "anthropic/claude-3-haiku"]

def get_all_answers(question):
    return {m: ask_model(m, question) for m in ai_models}

def evaluate(answers):
    for judge in judges:
        evaluation_prompt = "Evaluate which answer is most correct:\n" + str(answers)
        result = ask_model(judge, evaluation_prompt)
        print(f"\nJudge {judge} says:\n{result}")
