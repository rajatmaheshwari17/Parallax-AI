import openai
from googleapiclient.discovery import build
from anthropic import Anthropic

openai.api_key = ""
google_api_key = ""
cse_id = ""
ANTHROPIC_API_KEY = ""

def search_google(query: str) -> str:
    service = build("customsearch", "v1", developerKey=google_api_key)
    res = service.cse().list(q=query, cx=cse_id).execute()

    if 'items' in res:
        return res['items'][0]['snippet']
    else:
        return "Sorry, I couldn't find relevant information on the web."

def generate_gpt_response_with_rag(query: str) -> str:
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