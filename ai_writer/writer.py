import google.generativeai as genai
from config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-1.5-flash-latest")

def spin_content(content):
    prompt = f"Rephrase the following creatively like an author rewriting a novel chapter:\n\n{content}"
    response = model.generate_content(prompt)
    return response.text
