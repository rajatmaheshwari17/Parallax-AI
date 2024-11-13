from flask import Flask, request, jsonify
from flask_cors import CORS
from backend.models.chatgpt import chat_chatgpt
from backend.models.claude import chat_claude

app = Flask(__name__)
CORS(app)

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_message = data.get("message")
    selected_model = data.get("ai_model", "Chatgpt")
    strategy = data.get("strategy", "None")

    try:
        if selected_model.lower() == "chatgpt":
            assistant_message = chat_chatgpt(user_message, strategy)
        elif selected_model.lower() == "claude":
            assistant_message = chat_claude(user_message, strategy)
        # elif selected_model.lower() == "claude":
        #   assistant_message = chat_llama(user_message, strategy)
        # elif selected_model.lower() == "nematron":
        #   assistant_message = chat_nematron(user_message, strategy)
        else:
            assistant_message = "Please select a valid AI model."

        return jsonify({"message": assistant_message})

    except Exception as e:
        print("Error:", str(e))
        return jsonify({"error": "Unable to process the request"}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5001)