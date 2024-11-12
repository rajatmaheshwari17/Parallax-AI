import openai
from googleapiclient.discovery import build

# Set your OpenAI API key and Google API key
openai.api_key = ""  # Replace with your actual OpenAI API key
google_api_key = ""  # Replace with your Google API key
cse_id = ""  # Replace with your Custom Search Engine ID

# Function to fetch relevant info using Google Custom Search
def search_google(query: str) -> str:
    service = build("customsearch", "v1", developerKey=google_api_key)
    res = service.cse().list(q=query, cx=cse_id).execute()

    # Get the first result
    if 'items' in res:
        return res['items'][0]['snippet']
    else:
        return "Sorry, I couldn't find relevant information on the web."

def generate_response_with_rag(query: str) -> str:
    """
    Generate a response using RAG (retrieval-augmented generation).
    First, retrieve relevant information using Google Custom Search, then generate a response using GPT.
    """
    # Step 1: Retrieve relevant information using Google Search
    retrieved_info = search_google(query)
    
    # Step 2: Send the query along with the retrieved information to GPT-3
    prompt = f"Query: {query}\n\nRelevant information from Google search:\n{retrieved_info}\n\nAnswer:"

    try:
        # Generate response using OpenAI GPT-3 model
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Use the model you prefer (e.g., gpt-3.5-turbo)
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=150,
            n=1,
            temperature=0.7
        )
        print("API Response:", response)
        
        # Return the generated response
        return response['choices'][0]['message']['content'].strip()

    except Exception as e:
        print("Error:", e)  # Debugging output
        return "Sorry, there was an issue with generating the response."