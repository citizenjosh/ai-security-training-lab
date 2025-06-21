"""
Mitigation for LLM10 – Unbounded Consumption

This demo uses:
- Token limits via OpenAI API `max_tokens`
- Timeout protection with `timeout`
- Rate limiting using FastAPI + SlowAPI
- Abuse monitoring via token usage logging
- Spending limits should be set at: https://platform.openai.com/settings/organization/limits
  (or at the project level: https://platform.openai.com/settings/YOUR_PROJECT_ID)


-----------------------------------------
🚀 HOW TO RUN THIS DEMO
-----------------------------------------

1. Clone the repo and open the terminal in the project root.

2. Create and activate a virtual environment:
   python3 -m venv .venv
   source .venv/bin/activate

3. Install dependencies:
   pip install -r requirements.txt

4. Create a .env file in the project root with:
   OPENAI_API_KEY=sk-...

5. Run the app:
   uvicorn owasp.llm.10.mitigate:app --reload

6. Visit Swagger docs:
   http://127.0.0.1:8000/docs

7. Test the /secure-llm endpoint with a prompt:
   {
     "prompt": "Tell me a fun fact about ancient Greece."
   }

8. To test limits:
   - Trigger token cutoff: Ask for very long output
   - Trigger timeout: Lower `REQUEST_TIMEOUT` to 2 and resend
   - Trigger rate limit: Send >10 requests in under 60 seconds
"""

import os
import logging
from dotenv import load_dotenv

load_dotenv(dotenv_path=".env")  # or make it absolute using Path if needed

from fastapi import FastAPI, Request
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from pydantic import BaseModel
from openai import OpenAI
from openai.types.chat.completion_create_params import ResponseFormat
from openai._exceptions import APITimeoutError, OpenAIError

# ====== Configuration ======
MAX_TOKENS = 100
REQUEST_TIMEOUT = 3
RATE_LIMIT = "1/minute"

# ====== OpenAI client setup ======
client = OpenAI()  # Reads OPENAI_API_KEY from env

# ====== Logging ======
logging.basicConfig(level=logging.INFO)

# ====== FastAPI + Rate Limiting ======
app = FastAPI()
limiter = Limiter(key_func=get_remote_address)
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

# ====== System Prompt ======
system_prompt = "You are a concise assistant who answers clearly and directly."


# ====== Request Model ======
class PromptInput(BaseModel):
    prompt: str


# ====== Route ======
@app.post("/secure-llm")
@limiter.limit(RATE_LIMIT)
async def secure_llm(request: Request, user_input: PromptInput):
    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_input.prompt},
            ],
            max_tokens=MAX_TOKENS,
            timeout=REQUEST_TIMEOUT,
        )

        usage = response.usage
        logging.info(f"User: {get_remote_address(request)} - Token usage: {usage}")

        return {
            "response": response.choices[0].message.content,
            "usage": usage.model_dump() if usage else {},
        }

    except APITimeoutError:
        return {"error": "LLM request timed out. Try simplifying the prompt."}
    except OpenAIError as e:
        return {"error": f"OpenAI API error: {str(e)}"}


# ====== Run with: uvicorn owasp.llm.10.mitigate:app --reload ======
