import openai

openai.api_key = ""

# Function to generate a response using the Chain of Thought strategy
def generate_response_with_chain_of_thought(user_message):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Ensure you're using a valid chat model like GPT-3.5 or GPT-4
            messages=[
                {"role": "system", "content": "You are a logical assistant. Break down the problem and reason step by step before giving your final answer."},
                {"role": "user", "content": user_message}
            ]
        )
        print("API Response:", response)

        assistant_message = response['choices'][0]['message']['content']
        return assistant_message
    except Exception as e:
        print(f"Error in generating response: {e}")
        return "Error: Unable to generate response."