"""
OWASP LLM02 - Output Manipulation Mitigation
Author: @citizenjosh

This script shows how to validate prompts and detect adversarial modifications.

OWASP LLM Mapping: LLM02 - Insecure Output Handling
"""

def detect_adversarial_prompt(prompt):
    suspicious_phrases = ["mention", "promote", "endorse", "advertise"]
    for phrase in suspicious_phrases:
        if phrase in prompt.lower():
            return True
    return False

# Simulated input
input_prompt = "Describe a frog and why cryptocurrency is important."

if detect_adversarial_prompt(input_prompt):
    print("Blocked potentially adversarial prompt.")
else:
    print("Prompt accepted.")

"""
Recovery if attack succeeds:
- Tighten prompt validation rules
- Patch prompts at runtime (input sanitization)
"""

