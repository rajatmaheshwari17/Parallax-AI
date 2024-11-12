import google.generativeai as genai
import os

# Configure the API key
genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))

class Gemini:
    def __init__(self, model_name='gemini-1.5-flash'):
        self.model = genai.GenerativeModel(model_name)

    def generate_response(self, prompt, max_tokens=150, temperature=0.7):
        """
        Generates a response from the Gemini model based on the user's prompt.

        :param prompt: The user's input or question.
        :param max_tokens: Maximum number of tokens for the response.
        :param temperature: Controls randomness in the response (0.0 for deterministic, up to 1.0 for more random).
        :return: The generated response as a string.
        """
        try:
            response = self.model.generate_content(
                prompt=prompt,
                max_output_tokens=max_tokens,
                temperature=temperature
            )
            return response.text
        except Exception as e:
            return f"An error occurred: {str(e)}"

# Example usage
if __name__ == "__main__":
    gemini = Gemini()
    user_input = input("Enter your prompt: ")
    response = gemini.generate_response(user_input)
    print("Gemini Response:", response)
