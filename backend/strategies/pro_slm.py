import openai

openai.api_key = ""

def generate_response_with_pro_slm(user_message):
    try:
        # Pro-SLM strategy: Detailed and structured prompt
        detailed_prompt = f"""
        You are an expert assistant with extensive knowledge in various domains. Your task is to provide a comprehensive, clear, and well-rounded response to the following question. The answer should cover all relevant aspects of the topic, provide context or background where needed, and be informative without unnecessary elaboration. 
        Please ensure that your response is coherent, structured, and clear. You should aim to help the user understand the topic in depth while also maintaining brevity and clarity.

        Question: {user_message}
        """

        # Generate response using OpenAI's chat model (gpt-3.5-turbo)
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Use the chat model
            messages=[
                {"role": "system", "content": "You are a highly knowledgeable assistant. Your answers should be detailed, well-structured, and insightful."},
                {"role": "user", "content": detailed_prompt},
            ]
        )

        return response['choices'][0]['message']['content']
    
    except Exception as e:
        print(f"Error in generating response: {e}")
        return "Error: Unable to generate response with Pro-SLM."
