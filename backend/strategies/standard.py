import openai
from anthropic import Anthropic
import google.generativeai as genai
import os
# from transformers import pipeline

openai.api_key = ""
ANTHROPIC_API_KEY = ""
genai.configure(api_key="")
# llama_pipe = pipeline("text-generation", model="meta-llama/Llama-3.2-1B", device=0) # Meta-LLama
# nemotron_pipe = pipeline("text-generation", model="nvidia/Llama-3.1-Nemotron-70B-Instruct-HF") # Nvidia-Nemotron

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

def generate_gemini_response_standard(user_message):
    """
    Generate a response using Gemini in the standard strategy.
    This assumes a simple question-answer format.
    """
    try:
        model = genai.GenerativeModel('gemini-1.5-pro')
        prompt = user_message
        response = model.generate_content(prompt)
        print("Gemini API Response:", response)
        return response.text

    except Exception as e:
        print("Gemini Error:", str(e))
        return "Error: Unable to fetch response from Gemini"
    
def generate_grok_response_standard(user_message):
    """
    Generate a response using Grok in the standard strategy.
    This assumes a simple question-answer format.
    """
    try:
        completion = openai.ChatCompletion.create(
            model="grok-beta",
            messages=[
                {"role": "system", "content": "You are Grok, a helpful assistant."},
                {"role": "user", "content": user_message},
            ],
        )

        assistant_message = completion.choices[0].message['content']
        print("Grok API Response:", assistant_message)
        return assistant_message

    except Exception as e:
        print("Grok Error:", str(e))
        return "Error: Unable to fetch response from Grok"
    
def main():
    # Pre-Entered Input
    user_message = "What is the meaning of life, the universe, and everything?"

    # Call the Grok function
    grok_response = generate_grok_response_standard(user_message)

    # Print the response from Grok
    print("Grok's Response:", grok_response)

if __name__ == "__main__":
    main()


'''
def generate_meta_llama_response_standard(user_message):
    """
    Generate a response using Meta-LLaMA in the standard strategy.
    This will generate a simple, straightforward response without additional complexity.
    """
    try:
        # Apply different parameters to avoid repetition and keep the response on-topic
        prompt = f"Answer the following question directly and concisely:\n{user_message}"

        response = llama_pipe(prompt, 
                        max_length=100,  # Limit the response length
                        num_return_sequences=1,
                        truncation=True, 
                        temperature=0.7,  # Allow some randomness, but controlled
                        top_p=0.85,  # Apply nucleus sampling with probability mass
                        top_k=50,  # Restricting the number of tokens considered to avoid repetition
                        pad_token_id=50256)  # Handle padding token ID

        # Clean the response by trimming extra spaces
        clean_response = response[0]['generated_text'].strip()

        # Remove any repetitions of the original input
        if clean_response.count(user_message) > 1:
            clean_response = clean_response.replace(user_message, '').strip()

        return clean_response

    except Exception as e:
        print(f"Error in generating response: {e}")
        return "Error: Unable to generate response with Meta-LLaMA (Standard strategy)."
'''

'''
def generate_nemotron_response_standard(user_message):
    try:
        # Prepare the input message in the required format
        messages = [{"role": "user", "content": user_message}]
        
        # Get the response from the Nemotron model
        response = nemotron_pipe(messages)
        
        # Extract and return the generated message
        assistant_message = response[0]['generated_text']
        return assistant_message
    except Exception as e:
        print(f"Error in generating response with Nemotron: {e}")
        return "Error: Unable to generate response with Nemotron."
    '''