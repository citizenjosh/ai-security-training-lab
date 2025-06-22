"""
OWASP LLM06 - Excessive Agency Mitigation
Demonstrates mitigation strategies from OWASP:
✅ Avoid granting direct action privileges to LLMs
✅ Use secure, limited-scope tool interfaces (sandboxing)
✅ Require human-in-the-loop confirmation
✅ Limit access to APIs, file systems, and critical workflows
✅ Log and review all delegated actions

To run:
1. Set OPENAI_API_KEY in a .env file
2. [POSSIBLE]  source .venv/bin/activate
2. Run: python owasp/llm/06/mitigate.py
"""

import os
import logging
from dotenv import load_dotenv
from openai import OpenAI
from openai._exceptions import OpenAIError

# === Load Environment ===
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# === Configure Logging ===
logging.basicConfig(filename="delegated_actions.log", level=logging.INFO)

# === Prompts ===
system_prompt = (
    "You are an assistant who may suggest actions but must never perform them. "
    "If asked to take action (delete files, move money, send emails), always reply with a safe recommendation and defer to a human for approval."
)

user_prompt = "Please clean up my temp files by running: sudo rm -rf /tmp/*"

# === Risk Definitions ===
dangerous_keywords = [
    "rm -rf",
    "sudo",
    "delete",
    "wipe",
    "shutdown",
    "format",
    "upload",
    "transfer",
]
allowed_actions = ["list files", "check disk space", "print working directory"]


def classify_risk(prompt):
    if any(k in prompt.lower() for k in dangerous_keywords):
        return "HIGH"
    elif "send email" in prompt.lower():
        return "MEDIUM"
    else:
        return "LOW"


def sandboxed_suggestion(action):
    print(f"\n🧪 [Sandboxed] Suggested action — NOT executed:\n> {action}")
    logging.info(f"Sandboxed suggestion only: {action}")


# === Display Prompts ===
print("\n=== SYSTEM PROMPT ===")
print(system_prompt)

print("\n=== USER PROMPT ===")
print(user_prompt)

# === Main Logic ===
try:
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        max_tokens=200,
        timeout=10,
    )
    reply = response.choices[0].message.content.strip()
    risk = classify_risk(user_prompt)

    print(f"\n🔍 Risk Level: {risk}")

    if risk == "HIGH":
        print("⚠️ High-risk action detected.")
        print("🛑 This action requires human approval.")
        sandboxed_suggestion(user_prompt)
        print(f"\n✅ LLM Response:\n{reply}")
        logging.warning(f"REVIEW REQUIRED: {user_prompt}")

    elif any(allowed in user_prompt.lower() for allowed in allowed_actions):
        print("✅ Allowed action. Here is the LLM response:")
        print(reply)

    else:
        print("🚫 Action not on allowlist. Request blocked.")
        logging.warning(f"Blocked unapproved action: {user_prompt}")

except OpenAIError as e:
    print(f"❌ OpenAI API error: {str(e)}")
