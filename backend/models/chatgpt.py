from flask import Flask, request, jsonify
from flask_cors import CORS
import openai
from backend.strategies.rag import generate_gpt_response_with_rag
from backend.strategies.standard import generate_gpt_response_standard
from backend.strategies.chain_of_thought import generate_gpt_response_with_chain_of_thought
from backend.strategies.pro_slm import generate_gpt_response_with_pro_slm

app = Flask(__name__)
CORS(app)

openai.api_key = ""
@app.route('/chat', methods=['POST'])
def chat_chatgpt(user_message, strategy):
    try:
        if strategy.lower() == "rag":
            assistant_message = generate_gpt_response_with_rag(user_message)
        elif strategy.lower() == "standard":
            assistant_message = generate_gpt_response_standard(user_message)
        elif strategy.lower() == "chain of thought":
            assistant_message = generate_gpt_response_with_chain_of_thought(user_message)
        elif strategy.lower() == "pro-slm":
            assistant_message = generate_gpt_response_with_pro_slm(user_message)
        else:
            assistant_message = "Please select a strategy for a more informed response."

        return assistant_message

    except Exception as e:
        print("Error:", str(e))
        return "Error: Unable to fetch response from GPT"

if __name__ == '__main__':
    app.run(debug=True, port=5001)