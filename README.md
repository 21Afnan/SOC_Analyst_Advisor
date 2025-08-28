# 🛡️ SOC Analyst Advisor  

An **AI-powered SOC Analyst Advisor** that assists with **threat detection, incident response, and cybersecurity best practices**.  

**🔗 Live Demo:** [https://21afnan.github.io/SOC_Analyst_Advisor/](https://21afnan.github.io/SOC_Analyst_Advisor/)  

![GitHub stars](https://img.shields.io/github/stars/21afnan/SOC_Analyst_Advisor?style=social) 
![GitHub forks](https://img.shields.io/github/forks/21afnan/SOC_Analyst_Advisor?style=social) 
![License](https://img.shields.io/badge/license-MIT-blue.svg)  

---

## ✨ Features  

- 🚀 **Local AI hosting** using [Ollama](https://ollama.ai/) and **Mistral 7B**.  
- ⚡ **Backend built with FastAPI** for lightweight and fast API responses.  
- 💻 **Interactive Frontend** with a chatbot interface.  
- 🛡️ Designed for **SOC analysts** – quick insights, playbooks, and automation guidance.  

---

## 🛠️ Tech Stack  

| Component        | Technology Used         |
|------------------|------------------------|
| **Model**        | Mistral 7B (SOC-tuned) |
| **Local Hosting**| Ollama                 |
| **Backend**      | FastAPI (Python)       |
| **Frontend**     | HTML, CSS, JavaScript  |

---

## ⚙️ How It Works  

1. **Ollama runs Mistral 7B locally**, ensuring privacy and speed.  
2. **FastAPI acts as the backend**, exposing endpoints to communicate with the model.  
3. **Frontend UI** interacts with the backend API and displays responses in a chatbot format.  

---

## 🚀 Getting Started  

### **Prerequisites**
- Python 3.10+  
- Ollama installed and configured  
- Mistral 7B model downloaded locally  

### **Clone and Run**
```bash
# 1. Clone the repository
git clone https://github.com/21afnan/SOC_Analyst_Advisor.git
cd SOC_Analyst_Advisor

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the backend
uvicorn main:app --reload

# 4. Open the frontend
Open index.html in your browser or host via GitHub Pages


```
