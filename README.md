# SOC Analyst Advisor  

An **AI-powered SOC Analyst Advisor** that assists with **threat detection, incident response, and cybersecurity best practices**.  

**Live Demo:** [https://21afnan.github.io/SOC_Analyst_Advisor/](https://21afnan.github.io/SOC_Analyst_Advisor/)  

---

## Features  
- **Local AI hosting** using [Ollama](https://ollama.ai/) and **Mistral 7B** for SOC-focused responses.  
- **Backend built with FastAPI** to serve AI responses via an API.  
- **Frontend integration** for a clean and interactive chat interface.  
- Designed to **support SOC analysts** with quick insights, playbooks, and automation guidance.  

---

## Tech Stack  
- **Model:** Mistral 7B (fine-tuned for SOC use cases)  
- **Local Hosting:** Ollama  
- **Backend:** FastAPI  
- **Frontend:** HTML, CSS, JavaScript  

---

## How It Works  
1. **Ollama runs Mistral 7B locally**, ensuring private and fast inference.  
2. **FastAPI acts as the middle layer**, exposing endpoints to communicate with the model.  
3. **Frontend UI** fetches responses via API and displays them in a user-friendly chatbot interface.  

---

## Getting Started  

### Prerequisites  
- Python 3.10+  
- Ollama installed and configured  
- Mistral 7B model available locally  

### Installation  
1. Clone the repository:  
   ```bash
   git clone https://github.com/21afnan/SOC_Analyst_Advisor.git
   cd SOC_Analyst_Advisor
