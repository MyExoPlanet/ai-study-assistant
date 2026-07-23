import os

from dotenv import load_dotenv
import google.generativeai as genai


from pathlib import Path

env_path = Path(__file__).parent.parent / ".env"
load_dotenv(dotenv_path=env_path)

print("API Key:", os.getenv("GEMINI_API_KEY"))

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")


def summarize_text(text):
    prompt = f"""
    Summarize the following study material in simple language.
    Keep the important points and make it easy to revise.

    {text}
    """

    response = model.generate_content(prompt)

    return response.text