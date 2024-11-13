from flask import Flask, request, jsonify
from flask_cors import CORS
from anthropic import Anthropic
from backend.strategies.rag import generate_claude_response_with_rag
from backend.strategies.standard import generate_claude_response_standard
from backend.strategies.chain_of_thought import generate_claude_response_with_chain_of_thought
from backend.strategies.pro_slm import generate_claude_response_with_pro_slm
from backend.strategies.rag import search_google

app = Flask(__name__)
CORS(app)

ANTHROPIC_API_KEY = ""
client = Anthropic(api_key=ANTHROPIC_API_KEY)

@app.route('/chat/claude', methods=['POST'])
def chat_claude(user_message, strategy):
    """
    Handle chat requests for Claude with different strategies.
    Expected JSON payload: {
        "message": "user message here",
        "strategy": "strategy name here"
    }
    """
    try:
        if strategy.lower() == "rag":
            retrieved_info = search_google(user_message)
            assistant_message = generate_claude_response_with_rag(user_message, retrieved_info)
        elif strategy.lower() == "standard":
            assistant_message = generate_claude_response_standard(user_message)
        elif strategy.lower() == "chain of thought":
            assistant_message = generate_claude_response_with_chain_of_thought(user_message)
        elif strategy.lower() == "pro-slm":
            assistant_message = generate_claude_response_with_pro_slm(user_message)
        else:
            assistant_message = "Please select a valid strategy for Claude to generate a response."

        return assistant_message

    except Exception as e:
        print("Claude Error:", str(e))
        return "Error: Unable to fetch response from Claude"

if __name__ == '__main__':
    app.run(debug=True, port=5002) 