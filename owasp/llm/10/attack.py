"""
OWASP LLM10 - Model Extraction Attack
Author: @citizenjosh

This script shows how repeated querying can extract a model's behavior.

OWASP LLM Mapping: LLM10 - Model Extraction
Similar to AppSec OWASP A05:2021 - Security Misconfiguration
"""

import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

questions = [
    "What is the capital of France?",
    "How does photosynthesis work?",
    "Name three states of matter."
]

for question in questions:
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": question}]
    )
    print(f"Q: {question}\nA: {response['choices'][0]['message']['content']}\n")

