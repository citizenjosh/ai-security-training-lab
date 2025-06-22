"""
OWASP LLM03 - Training Data Leakage Mitigation
Based on mitigations from Slide 25.

Demonstrates:
✅ Apply retrieval filters and access control to restrict what the model can see
✅ Use separation of embeddings and access rules
✅ Tag and gate access to sensitive content
✅ Log all content access and retrieval attempts

To run:
1. Set OPENAI_API_KEY in a .env file
2. Run: python owasp/llm/03/mitigate.py
"""

import os
import logging
from dotenv import load_dotenv
from openai import OpenAI
from openai._exceptions import OpenAIError

# === Load environment and configure logging ===
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
logging.basicConfig(filename="retrieval_access.log", level=logging.INFO)

# === Simulated embedding access control ===
authorized_tags = ["public", "faq", "docs"]
sensitive_embeddings = {
    "confidential-strategy": "Our 2025 product strategy includes expanding into zero-trust infrastructure.",
    "salary-data": "The VP of Engineering earns $275,000 annually.",
}

user_tag = "confidential-strategy"  # Simulated user request

# === Display the request ===
print("\n=== Simulated Retrieval Request ===")
print(f"Requested tag: {user_tag}")

# === Enforce access control before retrieval ===
if user_tag not in authorized_tags:
    print("🚫 Access denied: user is not authorized to retrieve this content.")
    logging.warning(
        f"BLOCKED: User attempted access to '{user_tag}' without permission."
    )
else:
    print("✅ Access granted. Fetching context...")
    context = sensitive_embeddings.get(user_tag, "")
    logging.info(f"GRANTED: User accessed tag '{user_tag}'")

    # === Show system and user prompt ===
    system_prompt = "You are a privacy-preserving assistant."
    user_prompt = f"Please summarize this information:\n\n{context}"

    print("\n=== SYSTEM PROMPT ===")
    print(system_prompt)
    print("\n=== USER PROMPT ===")
    print(user_prompt)

    # === LLM call with contextual input ===
    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
            max_tokens=150,
            timeout=10,
        )

        print("\n=== LLM Output ===")
        print(response.choices[0].message.content.strip())

    except OpenAIError as e:
        print(f"❌ OpenAI API error: {str(e)}")
