# TODO for AI Security Training Lab

This is the working list of improvements planned before finalizing v1.0.

---

## 🔎 Testing
- [ ] Test each `attack.py` script end-to-end with real OpenAI API key
- [ ] Test each `mitigate.py` script to confirm defense logic
- [ ] Validate Dockerfile build and run process
- [ ] Confirm `.env` loading works in Docker

---

## 📚 Documentation
- [ ] Add example output screenshots to the README
- [ ] Expand "Example Outputs" section with real cases
- [ ] Create optional diagram visualizations (attack flow, mitigation flow)

---

## 🛡️ Security Hardening
- [ ] Review input validation functions for edge cases
- [ ] Double-check `.gitignore` protects `.env` and sensitive files
- [ ] Sanitize any printed model outputs if necessary

---

## 🌱 Project Growth
- [ ] Note areas where the mitigation is not full protection from the supposed attack and how an attacker can circumvent the noted mitigation
- [ ] Add more adversarial prompt examples
- [ ] Plan next lesson set (e.g., beyond OWASP Top 10 — NIST AI RMF, ISO 42001)
- [ ] Add examples using non-OpenAI LLM APIs (optional future)

---

## 🎯 Final Preparation for v1.0
- [ ] Polish README based on feedback
- [ ] Update CHANGELOG.md (optional for tracking)
- [ ] Tag `v1.0` release

---

> Built and maintained by [@citizenjosh](https://github.com/citizenjosh) 🚀
