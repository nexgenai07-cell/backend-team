import asyncio
import json
import logging
import re
import httpx
import google.generativeai as genai
# from google import genai
# from google.genai import types
from django.conf import settings

# Initialize module-level logger
logger = logging.getLogger(__name__)
# ─────────────────────────────────────────────
# Judge Prompt Template
# ─────────────────────────────────────────────
def build_judge_prompt(anonymized_responses: dict) -> str:
    """
    Constructs the master evaluation prompt containing anonymized responses.
    Ensures judges score blindly against specific quality metrics.
    """
    responses_text = ""
    for label, text in anonymized_responses.items():
        responses_text += f"\n--- Response {label} ---\n{text}\n"

    prompt = f"""You are an expert AI evaluator. Evaluate the following responses to a user prompt.

Responses to evaluate:
{responses_text}
Score each response from 0 to 10 based on:
- Accuracy (is it factually correct?)
- Relevance (does it answer the question?)
- Completeness (is it thorough?)
- Clarity (is it easy to understand?)
- Conciseness (is it to the point?)

IMPORTANT: Return ONLY a valid JSON object with response labels as keys and numeric scores as values.
Example format: {{"A": 8, "B": 9, "C": 7, "D": 6}}

Do not include any explanation, only the JSON object."""

    return prompt


# ─────────────────────────────────────────────
# Groq Judge
# ─────────────────────────────────────────────
async def groq_judge(client: httpx.AsyncClient, anonymized_responses: dict) -> dict:
    """
    Dispatches the prompt matrix to Groq (Llama model) to procure numerical rankings.
    """
    prompt = build_judge_prompt(anonymized_responses)
    try:
        # Low temperature parameter (0.1) enforces non-creative, deterministic scoring
        resp = await client.post(
            "https://api.groq.com/openai/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {settings.GROQ_API_KEY}",
                "Content-Type": "application/json",
            },
            json={
                "model": "llama-3.1-8b-instant",   
                "messages": [{"role": "user", "content": prompt}],
                "max_tokens": 200,
                "temperature": 0.1,  
            },
            timeout=60.0,
        )
        resp.raise_for_status()
        text = resp.json()["choices"][0]["message"]["content"]
        
        logger.info("Groq Judge completed evaluation successfully.")
        return parse_scores(text)

    except Exception as e:
        logger.exception(f"Groq Judge encountered an operational error during scoring: {str(e)}")
        return {}


# ─────────────────────────────────────────────
# Gemini Judge
# ─────────────────────────────────────────────
async def gemini_judge(anonymized_responses: dict) -> dict:
    """
    Dispatches the prompt matrix to the Gemini API utilizing the official SDK wrapper.
    """
    prompt = build_judge_prompt(anonymized_responses)
    try:
        # Configure SDK credentials locally
        genai.configure(api_key=settings.GEMINI_API_KEY)
        model = genai.GenerativeModel("gemini-2.5-flash")

        # Offload synchronous SDK call to an external thread worker pool to avoid event loop lag
        loop = asyncio.get_event_loop()
        response = await loop.run_in_executor(
            None,
            lambda: model.generate_content(prompt)
        )
        text = response.text
        
        logger.info("Gemini Judge completed evaluation successfully.")
        return parse_scores(text)

    except Exception as e:
        logger.exception(f"Gemini Judge encountered an operational error during scoring: {str(e)}")
        return {}


# ─────────────────────────────────────────────
# Helper: Parse JSON from judge output
# ─────────────────────────────────────────────
def parse_scores(text: str) -> dict:
    """
    Safely sanitizes and extracts raw numerical scores from judge payload strings.
    Utilizes fallback regex filters if the engine surrounds JSON with narrative prose.
    """
    try:
        # Initial extraction milestone try direct translation
        return json.loads(text.strip())
    except json.JSONDecodeError:
        # Fallthrough to backup strategy when raw text blocks flank the JSON object map
        logger.warning("Direct JSON serialization failed. Proceeding with string regex capture heuristics.")

    # Match JSON boundaries using standard non-nested object expression patterns
    match = re.search(r'\{[^{}]+\}', text)
    if match:
        try:
            raw = json.loads(match.group())
            # Enforce float castings across keys to preserve metric parity across evaluations
            return {k: float(v) for k, v in raw.items()}
        except Exception:
            logger.error("Regex parsing match isolated, but object conversion failed standard translation.")

    logger.critical(f"Parse Failure: Text payload format rejected from structural parsing. Content window: {text[:200]}")
    return {}


# ─────────────────────────────────────────────
# Main: Execute Both Judges in Parallel
# ─────────────────────────────────────────────
async def run_judges(anonymized_responses: dict) -> dict:
    """
    Executes multiple independent judge engines concurrently in parallel.
    Consolidates the scoring matrices and compiles an optimized mathematical average map.
    """
    logger.info("Initializing concurrent auditing process across active judge panels.")
    
    async with httpx.AsyncClient() as client:
        # Co-routine synchronization orchestrating unified performance runs
        groq_scores, gemini_scores = await asyncio.gather(
            groq_judge(client, anonymized_responses),
            gemini_judge(anonymized_responses),
        )

    final_scores = {}
    # Combine key maps into a unified set array to prevent data tracking gaps
    all_labels = set(list(groq_scores.keys()) + list(gemini_scores.keys()))

    for label in all_labels:
        scores = []
        if label in groq_scores:
            scores.append(float(groq_scores[label]))
        if label in gemini_scores:
            scores.append(float(gemini_scores[label]))
        
        # Calculate balanced average output rounded cleanly to index limits
        if scores:
            final_scores[label] = round(sum(scores) / len(scores), 2)

    logger.info(f"Consolidated score calculations completed for active labels: {list(final_scores.keys())}")
    
    return {
        "groq_scores": groq_scores,
        "gemini_scores": gemini_scores,
        "final_scores": final_scores,
    }