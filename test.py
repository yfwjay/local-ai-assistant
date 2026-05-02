import requests

response = requests.post("http://localhost:11434/api/generate", json={
    "model": "llama3.1:8b",
    "prompt": "Say hello!",
    "stream": False , 
    "keep-alive": 5 # unloads vram after 5 seconds
})

print(response.json()['response'])