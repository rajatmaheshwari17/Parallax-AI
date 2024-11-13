import openai
from anthropic import Anthropic
# from transformers import pipeline

openai.api_key = ""
ANTHROPIC_API_KEY = ""
# llama_pipe = pipeline("text-generation", model="meta-llama/Llama-3.2-1B", device=0)
# nemotron_pipe = pipeline("text-generation", model="nvidia/Llama-3.1-Nemotron-70B-Instruct-HF")

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
    
'''
def generate_meta_llama_response_with_chain_of_thought(user_message: str) -> str:
    try:
        prompt = f"""
        Please solve this problem using chain of thought reasoning. Break it down into steps:
        1. First, identify the key components of the problem
        2. Then, analyze each component systematically
        3. Show your reasoning for each step
        4. Finally, provide your conclusion

        Problem: {user_message}
        """

        response = meta_llama_pipe(prompt, 
                                   max_length=250,
                                   num_return_sequences=1,
                                   truncation=True, 
                                   temperature=0.7,
                                   top_p=0.85,
                                   top_k=50)
        
        clean_response = response[0]['generated_text'].strip()

        return clean_response

    except Exception as e:
        print(f"Error in generating response with Meta-LLaMA for Chain of Thought: {e}")
        return "Error: Unable to generate response with Meta-LLaMA for Chain of Thought."
'''

'''
def generate_nemotron_response_with_chain_of_thought(user_message: str) -> str:
    try:
        prompt = f"""
        Please solve this problem using chain of thought reasoning. Break it down into steps:
        1. First, identify the key components of the problem
        2. Then, analyze each component systematically
        3. Show your reasoning for each step
        4. Finally, provide your conclusion

        Problem: {user_message}
        """

        response = nemotron_pipe(prompt, 
                                 max_length=250,
                                 num_return_sequences=1,
                                 truncation=True, 
                                 temperature=0.7,
                                 top_p=0.85,
                                 top_k=50)
        
        clean_response = response[0]['generated_text'].strip()

        return clean_response

    except Exception as e:
        print(f"Error in generating response with Nemotron for Chain of Thought: {e}")
        return "Error: Unable to generate response with Nemotron for Chain of Thought."
'''