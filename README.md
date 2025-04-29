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

### Local Setup

1. Clone the repository:

```bash
git clone https://github.com/citizenjosh/ai-security-training-lab.git
cd ai-security-training-lab
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Configure your API key:
Copy ```.env.example``` to ```.env```
Insert your OpenAI API key inside ```.env```
```bash
cp .env.example .env
nano .env
```

4. Run any lesson:

```bash
python3 owasp/llm/01/attack.py
```



### Docker Setup
If you prefer, you can run the lab inside a Docker container.

1. Build the Docker image:
```bash
docker build -t ai-security-training-lab .
```
2. Run the container:
```bash
docker run --env-file .env -it ai-security-training-lab
```
✅ This ensures consistent environments for classrooms and workshops.



## ⚠️ Important Notice: API Key and Quotas

To run these exercises successfully, you must have an active OpenAI API key with available usage quota.

- **Free-tier accounts** have limited credits that may expire or run out quickly.
- If you see a `RateLimitError (429)` or `insufficient_quota` error, it means your account has exceeded its allowed usage.
- You can check your current quota and billing status at [https://platform.openai.com/account/usage](https://platform.openai.com/account/usage).

✅ **Recommended:**  
- Add a payment method to your OpenAI account for pay-as-you-go access.  
- Monitor your usage if running multiple exercises or workshops.

---

> *This project does not include any API credits or sponsorships. All usage costs are the responsibility of the user.*



## 🛠️ Tools
### Free Tools
* Guardrails AI<br />
https://github.com/ShreyaR/guardrails
* PromptInject<br />
    https://github.com/jthwjj/promptinject
* Cleanlab<br />
https://github.com/cleanlab/cleanlab
* SecretFlow<br />
https://secretflow.org/
* Opacus<br />
https://opacus.ai/
* TextAttack<br />
https://github.com/QData/TextAttack
* RobustBench<br />
https://robustbench.github.io/

## 🖼️ Example Outputs

## 🧠 Contribution Guidelines
Contributions are welcome!
1. Fork the repository
2. Create a new branch
3. Make your changes
4. Submit a pull request
5. Follow the Code of Conduct

## ⚖️ License
This project is licensed under the [MIT License](https://opensource.org/license/mit).

## 📢 Topics / Tags (recommended)
When setting your GitHub repository topics manually, consider adding:
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

Built and maintained by [@citizenjosh](https://github.com/citizenjosh) 🚀
