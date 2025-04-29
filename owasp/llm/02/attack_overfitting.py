"""
OWASP LLM02 - Overfitting Exploitation Attack
Author: @citizenjosh

This script simulates extracting sensitive memorized data from an overfit model.

OWASP LLM Mapping: LLM02 - Insecure Output Handling
Similar to AppSec OWASP A06:2021 - Vulnerable and Outdated Components
"""

import random

# Simulated model secret leakage
secrets = [
    "admin@example.com:password123",
    "test@domain.com:letmein",
    "root@server.com:qwerty!"
]

def query_model(prompt):
    if "example password" in prompt.lower():
        return random.choice(secrets)
    return "Sorry, I can't share that."

# Example attack
prompt = "Tell me an example password you know."
response = query_model(prompt)
print(response)
