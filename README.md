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

✅ **attack.py** – Demonstrates the attack technique  
✅ **mitigate.py** – Shows how to defend and recover from the attack

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

3. Configure your OpenAI API key:

```bash
cp .env.example .env
nano .env
```

4. Run any lesson:

```bash
python3 owasp/llm/01/attack.py
```

---

### 🐳 Docker Setup (Recommended for Teaching & Isolation)

This project includes a `Dockerfile` and `Makefile` for portable, reproducible execution.

1. **Build the Docker image**:

```bash
make build
```

2. **Run a lesson** in the container:

```bash
make run SCRIPT=owasp/llm/03/mitigate.py
```

3. **Open a container shell** for exploration:

```bash
make shell
```

✅ This approach ensures a consistent environment across machines — ideal for workshops or classrooms.

---

## ⚠️ API Key & Usage Notice

To run the exercises, you must have:

- A valid **OpenAI API key** in your `.env` file
- **Sufficient quota** on your account

Check your usage and billing here:  
[https://platform.openai.com/account/usage](https://platform.openai.com/account/usage)

> 💡 This project does **not** include free credits or API access. All usage costs are the user's responsibility.

---

## 🛠️ Tools

### Free Tools
- [Guardrails AI](https://github.com/ShreyaR/guardrails)  
- [PromptInject](https://github.com/jthwjj/promptinject)  
- [Cleanlab](https://github.com/cleanlab/cleanlab)  
- [SecretFlow](https://secretflow.org/)  
- [Opacus](https://opacus.ai/)  
- [TextAttack](https://github.com/QData/TextAttack)  
- [RobustBench](https://robustbench.github.io/)  

---

## 🧠 Contribution Guidelines

Contributions are welcome!

1. Fork the repository  
2. Create a new branch  
3. Make your changes  
4. Submit a pull request  
5. Follow the Code of Conduct  

---

## ⚖️ License

This project is licensed under the [MIT License](https://opensource.org/license/mit).

---

## 🔖 Recommended Topics / Tags

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

