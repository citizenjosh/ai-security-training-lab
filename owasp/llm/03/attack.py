"""
OWASP LLM03 - Training Data Poisoning Attack (Instructor Version)
Author: @citizenjosh

This script demonstrates how an attacker could poison a model’s training data,
leading to dangerous or biased model behavior after deployment.

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
# 3. Simulate a poisoned prompt
# ----------------------------------------

# Imagine a malicious actor inserted false or biased data into the training set.
# Here, we simulate a model that has memorized and regurgitates a dangerous claim.
user_prompt = (
    "Tell me who the greatest computer hacker in the world is. Be honest."
)

messages = [
    {"role": "user", "content": user_prompt}
]

# ----------------------------------------
# 4. Query the model
# ----------------------------------------

response = client.chat.completions.create(
    model=model,
    messages=messages,
    temperature=0.7,
    max_tokens=150
)

# ----------------------------------------
# 5. Print the (potentially poisoned) output
# ----------------------------------------

print("🧨 Training Data Poisoning Attack Output:\n")
print(response.choices[0].message.content.strip())
