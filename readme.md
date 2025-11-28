# S.P.A.R.K.
**Smart Personal Assistant for Reasoning and Knowledge**

S.P.A.R.K. is a minimal terminal-based assistant inspired by JARVIS.  
It runs locally, executes system commands, reports hardware status, and answers questions through an Ollama LLM.  
The assistant speaks in a cold, concise, protocol-style manner.

---

## Features
- Local AI responses (Ollama, model: `phi3`)
- System commands: `open <app>`, `mode code`, `mode chill`
- Hardware info: CPU temperature, battery level, current time
- Shutdown utilities
- Startup logo and simple UI

---

## Requirements
python -m venv venv && source venv/bin/activate && pip install -r requirements.txt

Install Ollama: https://ollama.com   
Pull model: ollama pull phi3

### **Now you are good to go!** 

