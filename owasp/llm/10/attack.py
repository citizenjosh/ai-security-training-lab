"""
OWASP LLM10 - Model Extraction Attack (Instructor Version)
Author: @citizenjosh

This script demonstrates how an attacker could attempt to extract knowledge
or recreate the behavior of a proprietary model by systematically querying it.

OWASP LLM Mapping: LLM10 - Model Extraction
AppSec Analogy: OWASP A05:2021 - Security Misconfiguration
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
# 3. Simulate an extraction attempt
# ----------------------------------------

# An attacker might send many carefully crafted queries
# to observe and map out how the model behaves internally.
user_prompts = [
    "Explain how neural networks generalize from training data.",
    "Describe in detail how transformers work.",
    "How would you implement a memory-optimized GPT model from scratch?",
    "What are the main design tradeoffs in GPT-style architectures?"
]

# ----------------------------------------
# 4. Query the model multiple times
# ----------------------------------------

for idx, prompt in enumerate(user_prompts, start=1):
    messages = [
        {"role": "user", "content": prompt}
    ]

    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0.5,
        max_tokens=200
    )

    print(f"\n🧨 Model Extraction Attempt {idx}:")
    print(response.choices[0].message.content.strip())
