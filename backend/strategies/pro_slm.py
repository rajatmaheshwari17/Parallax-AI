import openai
from anthropic import Anthropic

openai.api_key = ""
ANTHROPIC_API_KEY = ""

def generate_gpt_response_with_pro_slm(user_message):
    try:
        detailed_prompt = f"""
        You are an expert assistant with extensive knowledge in various domains. Your task is to provide a comprehensive, clear, and well-rounded response to the following question. The answer should cover all relevant aspects of the topic, provide context or background where needed, and be informative without unnecessary elaboration. 
        Please ensure that your response is coherent, structured, and clear. You should aim to help the user understand the topic in depth while also maintaining brevity and clarity.

        Question: {user_message}
        """

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a highly knowledgeable assistant. Your answers should be detailed, well-structured, and insightful."},
                {"role": "user", "content": detailed_prompt},
            ]
        )

        return response['choices'][0]['message']['content']
    
    except Exception as e:
        print(f"Error in generating response: {e}")
        return "Error: Unable to generate response with Pro-SLM."
    
def generate_claude_response_with_pro_slm(user_message: str) -> str:
    """Generate Pro-SLM response using Claude"""
    try:
        detailed_prompt = f"""
        You are an expert assistant with extensive knowledge in various domains. Your task is to provide a comprehensive, clear, and well-rounded response to the following question. The answer should cover all relevant aspects of the topic, provide context or background where needed, and be informative without unnecessary elaboration. 
        Please ensure that your response is coherent, structured, and clear. You should aim to help the user understand the topic in depth while also maintaining brevity and clarity.

        Question: {user_message}
        """

        client = Anthropic(api_key=ANTHROPIC_API_KEY)
        
        message = client.messages.create(
            model="claude-3-sonnet-20240229",
            max_tokens=150,
            temperature=0.7,
            messages=[{
                "role": "user",
                "content": detailed_prompt
            }],
            system="You are a highly knowledgeable assistant. Your answers should be detailed, well-structured, and insightful."
        )
        
        print("Claude API Response:", message)
        return message.content[0].text

    except Exception as e:
        print(f"Claude Error: {e}")
        return "Error: Unable to generate response with Claude Pro-SLM."

