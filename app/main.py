from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from fastapi.responses import FileResponse
import requests

app = FastAPI(title="SOC Analyst Ollama Backend")

# Allow frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

OLLAMA_API_URL = "http://127.0.0.1:11434/v1/completions"

class ChatRequest(BaseModel):
    message: str

def call_ollama_api(prompt: str) -> str:
    payload = {
        "model": "mistral:instruct",
        "prompt": prompt,
        "max_tokens": 300
    }
    try:
        res = requests.post(OLLAMA_API_URL, json=payload)
        res.raise_for_status()
        data = res.json()
        # Extract AI response text correctly
        return data.get("choices", [{}])[0].get("text", "No response from AI.")
    except Exception as e:
        return f"Error: {str(e)}"


@app.post("/api/chat")
async def chat_endpoint(request: ChatRequest):
    prompt = f"SOC Analyst Advisor: {request.message}"
    reply = call_ollama_api(prompt)
    return {"reply": reply}

@app.get("/")
async def root():
    return FileResponse("index.html")
