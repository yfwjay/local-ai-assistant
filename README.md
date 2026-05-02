# Local AI Assistant

A local AI assistant built with Python, Flask, and Ollama.
No API keys. No token limits. Runs entirely on your own machine.

## Why I Built This
As a software engineering student, I wanted a coding assistant
I could use for hours without worrying about token costs or privacy.
This project also gave me hands-on experience building a full-stack
AI-powered application from scratch.

## Features
- Chat interface via browser
- Powered by Llama 3.1 8B running locally via Ollama
- Fully private — nothing leaves your machine
- Optimized for NVIDIA GPU acceleration

## Tech Stack
- **Frontend:** HTML, CSS, Vanilla JavaScript
- **Backend:** Python, Flask
- **Model Runner:** Ollama
- **Model:** Llama 3.1 8B

## Hardware Used
- GPU: NVIDIA RTX 4060
- RAM: 32GB
- Storage: 1TB SSD

## Setup Instructions

### 1. Install Ollama
Download from [ollama.com](https://ollama.com) and install.

### 2. Pull the model
```bash
ollama pull llama3.1:8b
```

### 3. Clone this repo
```bash
git clone https://github.com/YOUR_USERNAME/local-ai-assistant.git
cd local-ai-assistant
```

### 4. Install dependencies
```bash
pip install -r requirements.txt
```

### 5. Run the app
```bash
python backend/app.py
```
Then open your browser at `http://localhost:5000`

## Project Status
Actively in development

## Roadmap
- [x] Ollama connection test
- [ ] Flask backend with chat API
- [ ] HTML/CSS chat interface
- [ ] Conversation memory
- [ ] File upload and context (RAG)
- [ ] Code execution sandbox
