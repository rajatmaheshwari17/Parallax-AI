import openai
from anthropic import Anthropic

openai.api_key = ""
ANTHROPIC_API_KEY = ""

def generate_gpt_response_with_chain_of_thought(user_message):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
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
    
def generate_claude_response_with_chain_of_thought(user_message: str) -> str:
    """Generate Chain of Thought response using Claude"""
    try:
        client = Anthropic(api_key=ANTHROPIC_API_KEY)
        
        prompt = f"""
        You are a logical assistant. Break down the problem and reason step by step before giving your final answer.

        Problem: {user_message}
        """
        
        message = client.messages.create(
            model="claude-3-sonnet-20240229",
            max_tokens=250,
            temperature=0.7,
            messages=[{
                "role": "user",
                "content": prompt
            }],
        )
        
        print("Claude API Response:", message)
        return message.content[0].text

    except Exception as e:
        print(f"Claude Error: {e}")
        return "Error: Unable to generate response with Claude Chain of Thought."
