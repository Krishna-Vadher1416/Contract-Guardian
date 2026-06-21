from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("GCP_API_KEY")

client = genai.Client(api_key=API_KEY)

def explain_clause(clause_text):
    prompt = f"""
    You are a legal assistant.

    Explain this clause in simple English.
    Also provide:
    - Risk level (Low/Medium/High)
    - Why it is risky

    Clause:
    {clause_text}
    """

    response = client.models.generate_content(
        model="gemini-flash-latest",
        contents=prompt
    )

    return response.text