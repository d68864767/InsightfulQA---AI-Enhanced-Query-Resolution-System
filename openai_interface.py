```python
import openai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Set OpenAI API key
openai.api_key = OPENAI_API_KEY

def generate_response(prompt, max_tokens=100):
    """
    Function to generate a response from OpenAI's GPT-3 or GPT-4 model.
    :param prompt: The question or statement to generate a response to.
    :param max_tokens: The maximum length of the response.
    :return: The generated response.
    """
    response = openai.Completion.create(
        engine="text-davinci-002",  # Use "text-davinci-002" for GPT-3 or the equivalent for GPT-4
        prompt=prompt,
        max_tokens=max_tokens
    )
    return response.choices[0].text.strip()

def translate_text(text, target_language):
    """
    Function to translate text to a target language using OpenAI's GPT-3 or GPT-4 model.
    :param text: The text to translate.
    :param target_language: The language to translate the text into.
    :return: The translated text.
    """
    prompt = f"{text} \\nTranslate the above text to {target_language}."
    translated_text = generate_response(prompt)
    return translated_text
```
