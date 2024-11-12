from flask import Flask, request, jsonify
from flask_cors import CORS
import openai
from backend.strategies.rag import generate_response_with_rag

# Initialize the Flask app
app = Flask(__name__)
CORS(app)
# Set your OpenAI API key
openai.api_key = ""

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_message = data.get("message")
    strategy = data.get("strategy", "None")

    try:
        # If RAG strategy is selected, use RAG to generate a response
        if strategy.lower() == "rag":
            assistant_message = generate_response_with_rag(user_message)
        else:
            assistant_message = "Please select a strategy for a more informed response."

        return jsonify({"message": assistant_message})

    except Exception as e:
        print("Error:", str(e))  # Print the error for debugging
        return jsonify({"error": "Unable to fetch response from GPT"}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5001)
