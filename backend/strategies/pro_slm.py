import openai
from anthropic import Anthropic
import google.generativeai as genai
# from transformers import pipeline

openai.api_key = ""
ANTHROPIC_API_KEY = ""
genai.configure(api_key="")
# llama_pipe = pipeline("text-generation", model="meta-llama/Llama-3.2-1B", device=0)
# nemotron_pipe = pipeline("text-generation", model="nvidia/Llama-3.1-Nemotron-70B-Instruct-HF")

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
    
def generate_gemini_response_with_pro_slm(query: str) -> str:
    """
    Generate a response using Gemini in the Pro_SLM strategy.
    First, retrieve relevant information using Google Custom Search, then generate a response using Gemini.
    """
    prompt = f"""
        You are an expert assistant with extensive knowledge in various domains. Your task is to provide a comprehensive, clear, and well-rounded response to the following question. The answer should cover all relevant aspects of the topic, provide context or background where needed, and be informative without unnecessary elaboration. 
        Please ensure that your response is coherent, structured, and clear. You should aim to help the user understand the topic in depth while also maintaining brevity and clarity.

        Question: {query}
        """
    
    try:
        model = genai.GenerativeModel('gemini-1.5-pro')
        response = model.generate_content(prompt)
        print("Gemini API Response:", response)
        return response.text

    except Exception as e:
        print("Gemini Error:", str(e))
        return "Error: Unable to fetch response from Gemini"

''' 
def generate_meta_llama_response_with_pro_slm(user_message: str) -> str:
    try:
        detailed_prompt = f"""
        You are an expert assistant with extensive knowledge in various domains. Your task is to provide a comprehensive, clear, and well-rounded response to the following question. The answer should cover all relevant aspects of the topic, provide context or background where needed, and be informative without unnecessary elaboration. 
        Please ensure that your response is coherent, structured, and clear. You should aim to help the user understand the topic in depth while also maintaining brevity and clarity.

        Question: {user_message}
        """

        response = meta_llama_pipe(detailed_prompt, 
                                   max_length=150,
                                   num_return_sequences=1,
                                   truncation=True, 
                                   temperature=0.7,
                                   top_p=0.85,  # Nucleus sampling
                                   top_k=50)
        
        clean_response = response[0]['generated_text'].strip()

        return clean_response

    except Exception as e:
        print(f"Error in generating response with Meta-LLaMA for Pro-SLM: {e}")
        return "Error: Unable to generate response with Meta-LLaMA for Pro-SLM."
'''

'''
def generate_nemotron_response_with_pro_slm(user_message: str) -> str:
    try:
        detailed_prompt = f"""
        You are an expert assistant with extensive knowledge in various domains. Your task is to provide a comprehensive, clear, and well-rounded response to the following question. The answer should cover all relevant aspects of the topic, provide context or background where needed, and be informative without unnecessary elaboration. 
        Please ensure that your response is coherent, structured, and clear. You should aim to help the user understand the topic in depth while also maintaining brevity and clarity.

        Question: {user_message}
        """

        response = nemotron_pipe(detailed_prompt, 
                                 max_length=150,
                                 num_return_sequences=1,
                                 truncation=True, 
                                 temperature=0.7,
                                 top_p=0.85,
                                 top_k=50)
        
        clean_response = response[0]['generated_text'].strip()

        return clean_response

    except Exception as e:
        print(f"Error in generating response with Nemotron for Pro-SLM: {e}")
        return "Error: Unable to generate response with Nemotron for Pro-SLM."
'''