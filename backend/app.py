from flask import Flask , request , jsonify , render_template
import requests

app = Flask(__name__ , template_folder = "../frontend")


# we create a conversation history - keeps context between messages

conversation_history = []

OLLAMA_URL = "http://localhost:11434/api/chat"
MODEL = "llama3.1:8b"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat" , methods = ["POST"])
def chat():
    user_message = request.json.get("message")

    if not user_message:
        return jsonify({"error": "No message provided"}) , 400
    

    # Add user message to history
    conversation_history.append({
        "role" : "user" , 
        "content" : user_message
    })

    # sell full conversation to Ollama
    response = requests.post(OLLAMA_URL , json = {
        "model" : MODEL ,
        "messages" : conversation_history , 
        "stream" : False , 
        "keep_alive" : "5m"
    })

    data = response.json()
    assistant_message = data['message']['content']

    # Add assistant response to history
    conversation_history.append({
        "role" : "assistant" , 
        "content" : "assistant_message"
    })
    
    return jsonify({"response" : assistant_message})

@app.route("/clear" , methods = ['POST'])
def clear():
    conversation_history.clear()
    return jsonify({"status" : "converstion cleared"})


if __name__ == "__main__":
    app.run(debug = True , port = 5000)