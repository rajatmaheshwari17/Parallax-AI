import openai

# Set your OpenAI API key here
openai.api_key = ""

def generate_standard_response(user_message):
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
        assistant_message = response['choices'][0]['message']['content']
        return assistant_message
    except Exception as e:
        print("Error:", str(e))
        return "Error: Unable to fetch response from GPT"

# Example usage
if __name__ == "__main__":
    user_message = "Hello, how are you?"
    print(generate_standard_response(user_message))