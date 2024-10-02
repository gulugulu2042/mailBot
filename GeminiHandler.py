import google.generativeai as genai

class GeminiHandler:
    def __init__(self, api_key):
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel("gemini-1.5-flash")

    def generate_summary(self, prompt):
        """
        Gets Gemini output for given text prompt.
        Uses Gemini 1.5 flash model

        Parameters:
        prompt (str): Input prompt

        Returns:
        str: Gemini text response
        """
        response = self.model.generate_content(prompt)
        return response.text
