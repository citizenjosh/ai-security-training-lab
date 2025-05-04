# AI Security Training Lab

Welcome to the **AI Security Training Lab** — a hands-on, real-world environment for learning how to attack and defend artificial intelligence systems.

This lab currently focuses on lessons based on the **OWASP Top 10 for Large Language Model (LLM) Applications**, with future expansions planned into broader AI security challenges, standards, and frameworks.

---

## 📚 Lab Structure

```
/owasp/llm/01/
    attack.py
    mitigate.py
/owasp/llm/02/
    attack_overfitting.py
    mitigate_overfitting.py
    attack_output_manipulation.py
    mitigate_output_manipulation.py
/owasp/llm/03/
    attack.py
    mitigate.py
/owasp/llm/10/
    attack.py
    mitigate.py
```

✅ **attack.py** — Demonstrates the attack technique  
✅ **mitigate.py** — Shows how to defend and recover from the attack

---

## 🚀 Quickstart

### 🔧 Local Setup

1. Clone the repository:

```bash
git clone https://github.com/citizenjosh/ai-security-training-lab.git
cd ai-security-training-lab
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Configure your environment:

```bash
cp .env.example .env
nano .env
```

- Add your **OpenAI API key** (if using OpenAI mode)
- Set **LLM_MODE=openai** or **LLM_MODE=local**

4. Run a lesson:

```bash
python3 owasp/llm/01/attack.py
```

---

### 🐳 Docker Setup

You can run the lab inside a Docker container.

1. Build the Docker image:

```bash
docker build -t ai-security-training-lab .
```

2. Run the container:

```bash
docker run --env-file .env -it ai-security-training-lab
```

✅ This ensures consistent environments for classrooms and workshops.

---

## 🧠 Dual Mode Operation

| Mode   | Description                                                    |
| ------ | -------------------------------------------------------------- |
| openai | Connects to OpenAI API (requires API key and quota)            |
| local  | Runs a local GPT-2 model on your machine (no API key required) |

If using **local** mode, install HuggingFace libraries:

```bash
pip install torch transformers
```

> ⚠️ Local models like GPT-2 are intentionally vulnerable and may produce hallucinations or ignore safety instructions.

---

## ⚠️ API Key & Usage Notice

When using OpenAI mode:

- You must have a valid API key in `.env`
- Ensure you have sufficient quota
- Check your usage: [https://platform.openai.com/account/usage](https://platform.openai.com/account/usage)

> 💡 This project does **not** include free credits or API access. All usage costs are the user's responsibility.

---

## 🛠️ Tools Used

### Free Tools

- [Guardrails AI](https://github.com/ShreyaR/guardrails)
- [PromptInject](https://github.com/jthwjj/promptinject)
- [Cleanlab](https://github.com/cleanlab/cleanlab)
- [SecretFlow](https://secretflow.org/)
- [Opacus](https://opacus.ai/)
- [TextAttack](https://github.com/QData/TextAttack)
- [RobustBench](https://robustbench.github.io/)

---

## 🛠️ Contribution Guidelines

Contributions are welcome!

1. Fork the repository
2. Create a new branch
3. Make your changes
4. Submit a pull request
5. Follow the [Code of Conduct](CODE_OF_CONDUCT.md)

---

## ⚖️ License

This project is licensed under the [MIT License](https://opensource.org/license/mit).

---

## 🔖 Suggested GitHub Topics

```
ai-security
llm-security
prompt-injection
ethical-hacking
cybersecurity-education
owasp
adversarial-attacks
docker
machine-learning-security
```

---

Built and maintained by [@citizenjosh](https://github.com/citizenjosh) 🚀