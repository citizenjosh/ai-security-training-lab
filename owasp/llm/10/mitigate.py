"""
OWASP LLM10 - Model Extraction Mitigation
Author: @citizenjosh

This script mitigates extraction attempts via query rate-limiting.

OWASP LLM Mapping: LLM10 - Model Extraction
"""

# Simulated rate limiting
MAX_QUERIES = 3
user_queries = 0

def can_respond():
    global user_queries
    if user_queries >= MAX_QUERIES:
        return False
    user_queries += 1
    return True

# Simulate queries
queries = ["Capital of France?", "Photosynthesis?", "Matter states?", "Extra query?"]

for q in queries:
    if can_respond():
        print(f"Responding to: {q}")
    else:
        print(f"Blocked: Too many queries.")

"""
Recovery if attack succeeds:
- Rotate model instances
- Adjust API behavior for high-frequency users
"""

