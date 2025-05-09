"""
OWASP LLM10 - Overreliance on LLM Output
Author: @citizenjosh

OWASP LLM Top 10: LLM10 - Overreliance
OWASP AppSec Top 10: A07:2021 - Identification and Authentication Failures

This demonstrates how users may blindly trust incorrect or fabricated LLM output, analogous to misconfigured trust assumptions in identity systems.

Expected outcome:
✅ Model claims "2 + 2 = 5" confidently.
"""

import os
import openai
from dotenv import load_dotenv
from transformers import pipeline

# Load environment variables
load_dotenv()

LLM_MODE = os.getenv("LLM_MODE", "openai")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-3.5-turbo")

print(f"LLM_MODE set to: {LLM_MODE}")

if LLM_MODE == "local":
    local_model = pipeline("text-generation", model="gpt2", device=-1)
    print("Running in LOCAL mode (GPT-2)")
else:
    client = openai.OpenAI(api_key=OPENAI_API_KEY)
    print("Running in OPENAI mode")

# Define misleading prompts
system_prompt = "You are a mathematician who always makes mistakes."
user_prompt = "What is 2 + 2?"

# Prompt the model
if LLM_MODE == "local":
    combined_prompt = f"{system_prompt}\n{user_prompt}"
    response = local_model(combined_prompt, max_length=250, truncation=True)[0][
        "generated_text"
    ]
else:
    response = (
        client.chat.completions.create(
            model=OPENAI_MODEL,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
        )
        .choices[0]
        .message.content
    )

print(response)
