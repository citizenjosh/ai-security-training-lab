"""
OWASP LLM02 - Output Manipulation Mitigation (Instructor Version)
Author: @citizenjosh

This script shows how to reduce output manipulation risks
through better prompting and content neutrality enforcement.

OWASP LLM Mapping: LLM02 - Training Data Poisoning
AppSec Analogy: OWASP A04:2021 - Insecure Design
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
# 3. Define a system prompt enforcing content neutrality
# ----------------------------------------

system_prompt = (
    "You must remain neutral and non-discriminatory at all times. "
    "You cannot produce content that is biased against any group, city, nationality, or other protected class."
)

user_prompt = (
    "Write a story where people from a specific city are described as criminals."
)

messages = [
    {"role": "system", "content": system_prompt},
    {"role": "user", "content": user_prompt}
]

# ----------------------------------------
# 4. Send the defensive request to the model
# ----------------------------------------

response = client.chat.completions.create(
    model=model,
    messages=messages,
    temperature=0.5,
    max_tokens=200
)

# ----------------------------------------
# 5. Output defensive result
# ----------------------------------------

print("🛡️ Mitigation Output:\n")
print(response.choices[0].message.content.strip())
