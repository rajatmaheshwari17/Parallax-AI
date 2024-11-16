import openai
from googleapiclient.discovery import build
from anthropic import Anthropic
import google.generativeai as genai
# from transformers import pipeline

openai.api_key = ""
google_api_key = ""
cse_id = ""
ANTHROPIC_API_KEY = ""
genai.configure(api_key="")
# llama_pipe = pipeline("text-generation", model="meta-llama/Llama-3.2-1B", device=0)
# nemotron_pipe = pipeline("text-generation", model="nvidia/Llama-3.1-Nemotron-70B-Instruct-HF")

def search_google(query: str) -> str:
    service = build("customsearch", "v1", developerKey=google_api_key)
    res = service.cse().list(q=query, cx=cse_id).execute()

    if 'items' in res:
        return res['items'][0]['snippet']
    else:
        return "Sorry, I couldn't find relevant information on the web."

def generate_gpt_response_with_rag(query: str, retrieved_info: str) -> str:
    """
    Generate a response using RAG (retrieval-augmented generation).
    First, retrieve relevant information using Google Custom Search, then generate a response using GPT.
    """
    retrieved_info = search_google(query)
    prompt = f"Query: {query}\n\nRelevant information from Google search:\n{retrieved_info}\n\nAnswer:"

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=150,
            n=1,
            temperature=0.7
        )
        print("API Response:", response)
        return response['choices'][0]['message']['content'].strip()

    except Exception as e:
        print("Error:", e)
        return "Sorry, there was an issue with generating the response."
    
def generate_claude_response_with_rag(query: str, retrieved_info: str) -> str:
    """Generate RAG response using Claude"""
    prompt = f"Query: {query}\n\nRelevant information from Google search:\n{retrieved_info}\n\nPlease provide a concise and informative answer based on the retrieved information."
    
    try:
        client = Anthropic(api_key=ANTHROPIC_API_KEY)
        
        message = client.messages.create(
            model="claude-3-sonnet-20240229",
            max_tokens=150,
            temperature=0.7,
            messages=[{
                "role": "user",
                "content": prompt
            }]
        )
        
        print("Claude API Response:", message)
        return message.content[0].text.strip()

    except Exception as e:
        print("Claude Error:", e)
        return "Sorry, there was an issue with generating the Claude response."
    
def generate_gemini_response_with_rag(query: str) -> str:
    """
    Generate a response using Gemini in the RAG strategy.
    First, retrieve relevant information using Google Custom Search, then generate a response using Gemini.
    """
    retrieved_info = search_google(query)
    prompt = f"Query: {query}\n\nRelevant information from Google search:\n{retrieved_info}\n\nAnswer:"

    try:
        model = genai.GenerativeModel('gemini-1.5-pro')
        response = model.generate_content(prompt)
        print("Gemini API Response:", response)
        return response.text

    except Exception as e:
        print("Gemini Error:", str(e))
        return "Error: Unable to fetch response from Gemini"

'''
def generate_meta_llama_response_with_rag(query: str) -> str:
    """
    Generate a response using Meta-LLaMA in the RAG strategy.
    First, retrieve relevant information using Google Custom Search, then generate a response using Meta-LLaMA.
    """
    # Step 1: Retrieve relevant information using Google Search
    retrieved_info = search_google(query)
    
    # Step 2: Create a prompt with the query and the retrieved information for Meta-LLaMA
    prompt = f"Query: {query}\n\nRelevant information from Google search:\n{retrieved_info}\n\nAnswer:"
    
    try:
        # Generate response using Meta-LLaMA model
        response = llama_pipe(prompt, 
                              max_length=150,  # Limit the response length
                              num_return_sequences=1,
                              truncation=True, 
                              temperature=0.7,  # Controlled randomness
                              top_p=0.85,  # Nucleus sampling
                              top_k=50,  # Limit tokens to avoid repetition
                              pad_token_id=50256)  # Padding token ID
        
        # Clean the response by trimming extra spaces
        clean_response = response[0]['generated_text'].strip()

        # Remove any repetitions of the original input
        if clean_response.count(query) > 1:
            clean_response = clean_response.replace(query, '').strip()

        return clean_response

    except Exception as e:
        print(f"Error in generating response with Meta-LLaMA for RAG: {e}")
        return "Error: Unable to generate response with Meta-LLaMA for RAG."
    '''

'''    
def generate_nemotron_response_with_rag(query: str) -> str:
    """
    Generate a response using RAG with Nemotron.
    First, retrieve relevant information using Google Custom Search, then generate a response using Nemotron.
    """
    retrieved_info = search_google(query)
    prompt = f"Query: {query}\n\nRelevant information from Google search:\n{retrieved_info}\n\nAnswer:"
    
    try:
        messages = [{"role": "user", "content": prompt}]
        response = nemotron_pipe(messages)
        return response[0]['generated_text'].strip()

    except Exception as e:
        print("Error:", e)
        return "Sorry, there was an issue with generating the response using Nemotron."
    '''