import os
import logging
from google import genai

# Initialize logger for tracking errors and warnings in production
logger = logging.getLogger(__name__)

def generate_gemini_response(prompt):
    """
    Sends a text prompt to the Gemini API and returns the generated text response.
    Exclusively fetches the API key from environment variables for production security.
    Handles legacy and newer model naming fallback to prevent 404/Not Found errors.
    """
    try:
        # Fetch the API key strictly from the environment variables (.env)
        api_key = os.getenv('GEMINI_API_KEY')
        
        # Validate if the API key exists
        if not api_key:
            logger.error("Gemini Error: GEMINI_API_KEY is missing from environment variables.")
            return "Gemini Error: API Key missing in configurations."

        # Initialize the Gemini Client using the latest SDK syntax
        client = genai.Client(api_key=api_key)

        try:
            # Try 1: Standard model naming format for google-genai SDK
            response = client.models.generate_content(
                model='gemini-2.5-flash',
                contents=prompt,
            )
            if response and response.text:
                return response.text
                
        except Exception as inner_e:
            # Fallback Try 2: Retry with 'models/' prefix if the strict model check fails
            logger.warning(f"Retrying with 'models/' prefix due to naming exception: {inner_e}")
            
            response = client.models.generate_content(
                model='models/gemini-2.5-flash',
                contents=prompt,
            )
            if response and response.text:
                return response.text

        # Return error if response is received but text could not be parsed
        return "Gemini Error: Could not extract text from response."

    except Exception as e:
        # Catch any global infrastructure or connection failures
        logger.error(f"Complete Gemini Integration Failure: {str(e)}")
        return f"Gemini Error: {str(e)}"