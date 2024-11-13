import openai
from anthropic import Anthropic

openai.api_key = ""
ANTHROPIC_API_KEY = ""

def generate_gpt_response_standard(user_message):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_message}
            ]
        )

        print("API Response:", response)
        assistant_message = response['choices'][0]['message']['content']
        return assistant_message
    except Exception as e:
        print("Error:", str(e))
        return "Error: Unable to fetch response from GPT"
    
def generate_claude_response_standard(user_message):
    """Generate response using Claude"""
    try:
        client = Anthropic(api_key=ANTHROPIC_API_KEY)
        
        message = client.messages.create(
            model="claude-3-sonnet-20240229",
            max_tokens=1024,
            messages=[{
                "role": "user",
                "content": user_message
            }]
        )
        
        print("Claude API Response:", message)
        return message.content[0].text
    except Exception as e:
        print("Claude Error:", str(e))
        return "Error: Unable to fetch response from Claude"

if __name__ == "__main__":
    user_message = "Hello, how are you?"
    print(generate_gpt_response_standard(user_message))
    print(generate_claude_response_standard(user_message))
