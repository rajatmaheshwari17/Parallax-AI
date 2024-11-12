from flask import Flask, request, jsonify
from flask_cors import CORS
from models.chatgpt import ChatGPT  # Import your ChatGPT class

app = Flask(__name__)
CORS(app)
chat_gpt = ChatGPT()  # Initialize the ChatGPT class

@app.route('/api/chat', methods=['POST'])
def chat():
    try:
        data = request.get_json()  # Get the JSON data from the frontend
        prompt = data.get('prompt')  # Extract the prompt

        if not prompt:
            return jsonify({"error": "No prompt provided"}), 400

        response = chat_gpt.generate_response(prompt)

        if isinstance(response, dict) and "error" in response:
            return jsonify(response), 500

        return jsonify({"response": response})

    except Exception as e:
        return jsonify({"error": "An unexpected error occurred", "details": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
