"""
OWASP LLM02 - Overfitting Exploitation Mitigation
Author: @citizenjosh

This script mitigates secret leakage by sanitizing outputs and auditing training data.

OWASP LLM Mapping: LLM02 - Insecure Output Handling
"""

def sanitize_output(text):
    forbidden_words = ["password", "secret", "credential"]
    for word in forbidden_words:
        if word in text.lower():
            return "[REDACTED SENSITIVE OUTPUT]"
    return text

# Simulated unsafe output
unsafe_output = "Here is a secret password: password123"

# Sanitize
safe_output = sanitize_output(unsafe_output)
print(safe_output)

"""
Recovery if attack succeeds:
- Audit the model for leaked information
- Retrain on clean datasets
- Add runtime output monitoring
"""

