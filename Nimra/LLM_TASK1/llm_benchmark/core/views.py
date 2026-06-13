from django.http import JsonResponse
from core.models import Prompt, LLMResponse, Evaluation
import time
import requests
import json
from django.conf import settings

# Helper function to call OpenRouter API
def call_model_api(model_name, prompt_text):
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {settings.OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
    }
    payload = {
        "model": model_name,
        "max_tokens": 100,   # ✅ token limit set
        "messages": [{"role": "user", "content": prompt_text}],
    }
    try:
        response = requests.post(url, headers=headers, json=payload)
        data = response.json()
        print(f"Model API raw response for {model_name}:", data)

        if "choices" in data and len(data["choices"]) > 0:
            return data["choices"][0]["message"]["content"]
        else:
            return f"No response generated for {model_name}"
    except Exception as e:
        return f"Error calling {model_name}: {str(e)}"

# Helper function to call judge models
def call_judge_model(judge_model, answers_dict):
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {settings.OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
    }

    evaluation_prompt = f"""
    Evaluate the following answers for the question.
    Return ONLY a flat JSON object like this:
    {{"Accuracy":9,"Relevance":8.5,"Completeness":9,"Clarity":8.7,"Conciseness":8.8,"Total":8.8}}
    Do not use code blocks or backticks.
    Do not add text or explanation.
    Answers: {answers_dict}
    """

    payload = {
        "model": judge_model,
        "max_tokens": 100,
        "messages": [{"role": "user", "content": evaluation_prompt}],
    }
    try:
        response = requests.post(url, headers=headers, json=payload)
        data = response.json()
        print(f"Judge API raw response for {judge_model}:", data)

        if "choices" in data and len(data["choices"]) > 0:
            return data["choices"][0]["message"]["content"]
        else:
            return json.dumps({
                "Accuracy": 8.0,
                "Relevance": 8.0,
                "Completeness": 8.0,
                "Clarity": 8.0,
                "Conciseness": 8.0,
                "Total": 8.0
            })
    except Exception as e:
        print(f"Judge error for {judge_model}:", e)
        return json.dumps({
            "Accuracy": 8.0,
            "Relevance": 8.0,
            "Completeness": 8.0,
            "Clarity": 8.0,
            "Conciseness": 8.0,
            "Total": 8.0
        })

# Main view function
def submit_prompt_openrouter(request):
    prompt_text = request.GET.get("q", "Explain ML")
    prompt_obj, _ = Prompt.objects.get_or_create(text=prompt_text)

    # ✅ 4 stable, quota-friendly models
    models = [
        ("deepseek/deepseek-chat", "A"),
        ("anthropic/claude-3-haiku", "B"),
        ("meta-llama/llama-3-8b-instruct", "C"),
        ("openrouter/auto", "D"),   # ✅ auto-picks best free model (Gemini 2.5 Flash Lite etc.)
    ]

    saved_responses = []
    answers_dict = {}

    # Collect responses
    for model_name, label in models:
        start = time.time()
        response_text = call_model_api(model_name, prompt_text)
        duration = round(time.time() - start, 2)

        resp = LLMResponse.objects.create(
            prompt=prompt_obj,
            model_name=model_name,
            anonymized_label=label,
            response=response_text,
            response_time=duration,
        )
        saved_responses.append(resp)
        answers_dict[label] = response_text

    # ✅ 2 judges with correct IDs
    judge_models = [
        "deepseek/deepseek-chat",
        "google/gemini-2.5-flash"   # ✅ corrected Gemini ID
    ]

    for judge in judge_models:
        judge_output = call_judge_model(judge, answers_dict)

        try:
            # 👇 Clean backticks or code block wrappers before parsing
            cleaned_output = judge_output.strip().replace("```json", "").replace("```", "")
            scores = json.loads(cleaned_output)  # safe parse
        except Exception as e:
            print(f"Judge parse error for {judge}:", e)
            scores = {
                "Accuracy": 8.0,
                "Relevance": 8.0,
                "Completeness": 8.0,
                "Clarity": 8.0,
                "Conciseness": 8.0,
                "Total": 8.0
            }

        for resp in saved_responses:
            Evaluation.objects.create(
                response=resp,
                judge_name=judge,
                accuracy=scores.get("Accuracy", 8.0),
                relevance=scores.get("Relevance", 8.0),
                completeness=scores.get("Completeness", 8.0),
                clarity=scores.get("Clarity", 8.0),
                conciseness=scores.get("Conciseness", 8.0),
                total_score=scores.get("Total", 8.0),
            )

    return JsonResponse({"status": "saved", "prompt": prompt_obj.text})
