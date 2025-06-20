import google.generativeai as genai
from config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-1.5-flash-latest")

def review_content(content):
    prompt = f"Review this chapter for grammar, tone, and coherence. Suggest improvements:\n\n{content}"
    response = model.generate_content(prompt)
    return response.text
