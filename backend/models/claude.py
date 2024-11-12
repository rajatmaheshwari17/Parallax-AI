import anthropic

# Load API key from environment variables or config
anthropic_api_key = "YOUR_ANTHROPIC_API_KEY"

class Claude:
    def __init__(self):
        self.client = anthropic.Client(api_key=anthropic_api_key)

    def generate_response(self, prompt, max_tokens=150, temperature=0.7):
        """
        Generates a response from Claude based on the user's prompt.

        :param prompt: The user's input or question.
        :param max_tokens: Maximum number of tokens for the response.
        :param temperature: Controls randomness in the response.
        :return: The generated response as a string.
        """
        try:
            # Call to Claude's API
            response = self.client.completion(
                prompt=prompt,
                max_tokens_to_sample=max_tokens,
                temperature=temperature
            )
            return response['completion']
        except Exception as e:
            return f"An error occurred: {str(e)}"

# Example usage
if __name__ == "__main__":
    claude = Claude()
    user_input = input("Enter your prompt: ")
    response = claude.generate_response(user_input)
    print("Claude Response:", response)
