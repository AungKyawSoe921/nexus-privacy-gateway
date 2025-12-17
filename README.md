# 🛡️ Nexus Privacy Gateway

> **A Hybrid AI Router that protects sensitive data by intelligently switching between Google Gemini (Cloud) and Ollama (Local).**

---

## ⚡ The Concept
Companies want to use powerful AI like Gemini but cannot risk sending private secrets (like financial data) to the cloud.

**Nexus solves this by acting as a "Traffic Cop":**
* ✅ **Safe Questions** (Coding, History) → Routed to **Google Gemini** (Fast & Cheap).
* 🔒 **Secret Questions** (Internal Salaries, Projects) → Routed to **Local Llama 3** (100% Private).

---

## 🏗️ Architecture

| Component | Technology | Role |
| :--- | :--- | :--- |
| **The Router** | Python + TinyLlama | Decides if data is SAFE or PRIVATE. |
| **Public Brain** | Google Gemini 1.5 | Handles general knowledge. |
| **Private Brain** | Ollama (Local) | Handles sensitive internal data. |

---

## 🛠️ Tech Stack
* **Python 3.10+**
* **LangChain** (Orchestration)
* **Ollama** (Local LLM Server)
* **Google Generative AI** (Cloud API)

---

## 🚀 Quick Start

### 1. Prerequisites
You need [Ollama](https://ollama.com/) installed and running.
```bash
ollama run tinyllama
2. Installation
Bash

git clone [https://github.com/AungKyawSoe921/nexus-privacy-gateway.git](https://github.com/AungKyawSoe921/nexus-privacy-gateway.git)
cd nexus-privacy-gateway
pip install -r requirements.txt
3. Setup Keys
Create a .env file and add your Google key:

Code snippet

GEMINI_API_KEY=your_actual_api_key_here
4. Run It
Bash

python nexus.py
📸 Demo Scenarios
User asks: "Write a Python script."

Nexus: 🟢 [ROUTE: PUBLIC] Sending to Google Gemini...

User asks: "How do I pay at Orbital Coffee?"

Nexus: 🔒 [ROUTE: PRIVATE] Processing locally. Data never left the machine.

👨‍💻 Author
Aung Kyaw Soe Exploring Hybrid AI Architectures & Privacy Engineering.
