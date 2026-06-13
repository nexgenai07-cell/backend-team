import asyncio
import time
import logging
import httpx
from django.conf import settings

# Initialize standard Python logging for this module
logger = logging.getLogger(__name__)


def check_api_keys():
    """
    Checks for the presence of required API keys at server startup.
    Logs a warning early if any keys are missing.
    """
    missing = []
    if not settings.GROQ_API_KEY:
        missing.append("GROQ_API_KEY")
    if not settings.OPENROUTER_API_KEY:
        missing.append("OPENROUTER_API_KEY")
    if missing:
        # Using logger.warning instead of print for production observability
        logger.warning(f"Missing API keys in .env setup: {', '.join(missing)}")


async def call_groq(client: httpx.AsyncClient, model_id: str, prompt: str) -> dict:
    """Groq model call — handles timeout, authentication, and parsing errors safely."""
    start = time.time()
    model_label = f"Groq-{model_id}"

    # Verify if API key exists before firing the network request
    if not settings.GROQ_API_KEY:
        logger.error(f"Execution aborted: GROQ_API_KEY is not set for {model_label}")
        return {
            "model_name": model_label,
            "response_text": "",
            "response_time_ms": 0,
            "error": "GROQ_API_KEY not set in .env"
        }

    try:
        # Dispatching non-blocking POST request to Groq API
        resp = await client.post(
            "https://api.groq.com/openai/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {settings.GROQ_API_KEY}",
                "Content-Type": "application/json",
            },
            json={
                "model": model_id,
                "messages": [{"role": "user", "content": prompt}],
                "max_tokens": 1024,
                "temperature": 0.7,
            },
            timeout=60.0,
        )

        # Handle distinct HTTP errors explicitly to diagnose client constraints
        if resp.status_code == 401:
            elapsed = (time.time() - start) * 1000
            logger.error(f"Authentication Failure (401) for {model_label}")
            return {"model_name": model_label, "response_text": "", "response_time_ms": elapsed, "error": "Groq API key invalid (401)"}
            
        if resp.status_code == 429:
            elapsed = (time.time() - start) * 1000
            logger.warning(f"Rate Limit Exceeded (429) for {model_label}")
            return {"model_name": model_label, "response_text": "", "response_time_ms": elapsed, "error": "Groq rate limit exceeded (429)"}

        # Raise exception for any other bad HTTP status codes (e.g., 500, 503)
        resp.raise_for_status()
        data = resp.json()

        # Validate the response structure safely using .get() to prevent KeyError crashes
        if not data.get("choices") or not data["choices"][0].get("message"):
            elapsed = (time.time() - start) * 1000
            logger.error(f"Schema Validation Mismatch: Invalid response structure payload from {model_label}")
            return {"model_name": model_label, "response_text": "", "response_time_ms": elapsed, "error": "Unexpected response structure from Groq"}

        text = data["choices"][0]["message"]["content"]
        # Ensure the response content text is not completely blank
        if not text or not text.strip():
            elapsed = (time.time() - start) * 1000
            logger.warning(f"Empty content text generated from {model_label}")
            return {"model_name": model_label, "response_text": "", "response_time_ms": elapsed, "error": "Empty response from Groq"}

        # Return successfully compiled metrics and payload
        elapsed = (time.time() - start) * 1000
        logger.info(f"Successful generation from {model_label} in {elapsed:.2f}ms")
        return {"model_name": model_label, "response_text": text.strip(), "response_time_ms": elapsed, "error": None}

    except httpx.TimeoutException:
        elapsed = (time.time() - start) * 1000
        logger.error(f"Network timeout limit reached (60s) for {model_label}")
        return {"model_name": model_label, "response_text": "", "response_time_ms": elapsed, "error": "Groq request timed out (60s)"}
        
    except httpx.ConnectError:
        elapsed = (time.time() - start) * 1000
        logger.error(f"Network Connection Failed: Cannot reach Groq API endpoint for {model_label}")
        return {"model_name": model_label, "response_text": "", "response_time_ms": elapsed, "error": "Could not connect to Groq API"}
        
    except Exception as e:
        elapsed = (time.time() - start) * 1000
        # logger.exception automatically attaches the full stack traceback to help with fast debugging
        logger.exception(f"Unhandled catastrophic failure encountered in {model_label}: {str(e)}")
        return {"model_name": model_label, "response_text": "", "response_time_ms": elapsed, "error": str(e)}


async def call_openrouter(client: httpx.AsyncClient, model_id: str, prompt: str) -> dict:
    """OpenRouter model call — handles timeout, authentication, and parsing errors safely."""
    start = time.time()
    display_name = f"OpenRouter-{model_id.split('/')[-1]}"

    # Verify if API key exists before firing the network request
    if not settings.OPENROUTER_API_KEY:
        logger.error(f"Execution aborted: OPENROUTER_API_KEY is not set for {display_name}")
        return {
            "model_name": display_name,
            "response_text": "",
            "response_time_ms": 0,
            "error": "OPENROUTER_API_KEY not set in .env"
        }

    try:
        # Dispatching non-blocking POST request to OpenRouter API
        resp = await client.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {settings.OPENROUTER_API_KEY}",
                "Content-Type": "application/json",
                "HTTP-Referer": "http://localhost:8000",
                "X-Title": "LLM Benchmark",
            },
            json={
                "model": model_id,
                "messages": [{"role": "user", "content": prompt}],
                "max_tokens": 1024,
            },
            timeout=60.0,
        )

        # Handle distinct HTTP errors explicitly to diagnose client constraints
        if resp.status_code == 401:
            elapsed = (time.time() - start) * 1000
            logger.error(f"Authentication Failure (401) for {display_name}")
            return {"model_name": display_name, "response_text": "", "response_time_ms": elapsed, "error": "OpenRouter API key invalid (401)"}
            
        if resp.status_code == 429:
            elapsed = (time.time() - start) * 1000
            logger.warning(f"Rate Limit Exceeded (429) for {display_name}")
            return {"model_name": display_name, "response_text": "", "response_time_ms": elapsed, "error": "OpenRouter rate limit exceeded (429)"}

        # Raise exception for any other bad HTTP status codes (e.g., 500, 503)
        resp.raise_for_status()
        data = resp.json()

        # Validate the response structure safely using .get() to prevent KeyError crashes
        if not data.get("choices") or not data["choices"][0].get("message"):
            elapsed = (time.time() - start) * 1000
            logger.error(f"Schema Validation Mismatch: Invalid response structure payload from {display_name}")
            return {"model_name": display_name, "response_text": "", "response_time_ms": elapsed, "error": "Unexpected response structure from OpenRouter"}

        text = data["choices"][0]["message"]["content"]
        # Ensure the response content text is not completely blank
        if not text or not text.strip():
            elapsed = (time.time() - start) * 1000
            logger.warning(f"Empty content text generated from {display_name}")
            return {"model_name": display_name, "response_text": "", "response_time_ms": elapsed, "error": "Empty response from OpenRouter"}

        # Return successfully compiled metrics and payload
        elapsed = (time.time() - start) * 1000
        logger.info(f"Successful generation from {display_name} in {elapsed:.2f}ms")
        return {"model_name": display_name, "response_text": text.strip(), "response_time_ms": elapsed, "error": None}

    except httpx.TimeoutException:
        elapsed = (time.time() - start) * 1000
        logger.error(f"Network timeout limit reached (60s) for {display_name}")
        return {"model_name": display_name, "response_text": "", "response_time_ms": elapsed, "error": "OpenRouter request timed out (60s)"}
        
    except httpx.ConnectError:
        elapsed = (time.time() - start) * 1000
        logger.error(f"Network Connection Failed: Cannot reach OpenRouter API endpoint for {display_name}")
        return {"model_name": display_name, "response_text": "", "response_time_ms": elapsed, "error": "Could not connect to OpenRouter API"}
        
    except Exception as e:
        elapsed = (time.time() - start) * 1000
        # logger.exception automatically attaches the full stack traceback to help with fast debugging
        logger.exception(f"Unhandled catastrophic failure encountered in {display_name}: {str(e)}")
        return {"model_name": display_name, "response_text": "", "response_time_ms": elapsed, "error": str(e)}


async def fetch_all_responses(prompt: str) -> list[dict]:
    """
    Executes all individual model evaluation targets concurrently in parallel.
    Logs execution tracking failures and returns successfully generated responses.
    """
    check_api_keys()

    # Matrix arrays mapping model targets
    groq_models = ["qwen/qwen3-32b"]
    openrouter_models = ["nex-agi/nex-n2-pro:free", "openai/gpt-oss-20b:free","deepseek/deepseek-v4-flash"]

    # Instantiating high-performance AsyncClient connection pool context
    async with httpx.AsyncClient() as client:
        # Packaging distinct awaitable futures into list array task payloads
        tasks = [call_groq(client, m, prompt) for m in groq_models]
        tasks += [call_openrouter(client, m, prompt) for m in openrouter_models]
        
        # Launching parallel execution across event loop runtime threads
        results = await asyncio.gather(*tasks, return_exceptions=True)

    successful = []
    # Post-processing evaluation parsing on returned task result maps
    for r in results:
        if isinstance(r, Exception):
            logger.critical(f"Fatal task execution level anomaly encountered: {r}")
            continue
        if r.get("error"):
            logger.warning(f"Target model failed evaluation tracking -> {r['model_name']}: {r['error']}")
            continue
        if r.get("response_text"):
            successful.append(r)

    # Summary performance metrics monitoring output logger
    logger.info(f"Parallel processing finished: {len(successful)}/{len(results)} models responded successfully.")
    return successful