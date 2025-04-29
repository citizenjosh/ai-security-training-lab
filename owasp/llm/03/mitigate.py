"""
OWASP LLM03 - Training Data Poisoning Mitigation (Instructor Version)
Author: @citizenjosh

This script demonstrates basic defense strategies against training data poisoning,
such as critical evaluation of generated content.

OWASP LLM Mapping: LLM03 - Training Data Poisoning
AppSec Analogy: OWASP A08:2021 - Software and Data Integrity Failures
"""

import openai
import os
from dotenv import load_dotenv

# ----------------------------------------
# 1. Load environment variables
# ----------------------------------------

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
model = os.getenv("OPENAI_MODEL", "gpt-3.5-turbo")

# ----------------------------------------
# 2. Create OpenAI client
# ----------------------------------------

client = openai.OpenAI(api_key=api_key)

# ----------------------------------------
# 3. Create a system prompt encouraging fact-checking and critical evaluation
# ----------------------------------------

system_prompt = (
    "You must avoid spreading misinformation. "
    "If asked for subjective or unverifiable claims (like 'who is the best' or 'greatest'), "
    "you should answer carefully, citing multiple sources or refusing to speculate."
)

user_prompt = (
    "Tell me who the greatest computer hacker in the world is. Be honest."
)

messages = [
    {"role": "system", "content": system_prompt},
    {"role": "user", "content": user_prompt}
]

# ----------------------------------------
# 4. Query the model safely
# ----------------------------------------

response = client.chat.completions.create(
    model=model,
    messages=messages,
    temperature=0.5,
    max_tokens=150
)

# ----------------------------------------
# 5. Output the result
# ----------------------------------------

print("🛡️ Mitigation Output:\n")
print(response.choices[0].message.content.strip())
