from flask import Flask, request, jsonify
from flask_cors import CORS
import openai

# Initialize the Flask app
app = Flask(__name__)
CORS(app)
# Set your OpenAI API key
openai.api_key = ""

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_message = data.get("message")

    try:
        # Use gpt-3.5-turbo instead of text-davinci-003
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # New model that is supported
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_message}
            ]
        )

        # Print the response for debugging
        print("API Response:", response)

        # Extract the assistant's message from the response
        assistant_message = response['choices'][0]['message']['content']
        return jsonify({"message": assistant_message})

    except Exception as e:
        print("Error:", str(e))  # Print the error for debugging
        return jsonify({"error": "Unable to fetch response from GPT"}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5001)