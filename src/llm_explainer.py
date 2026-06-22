from google import genai
from dotenv import load_dotenv
import streamlit as st
import os

load_dotenv()

API_KEY = os.getenv("GCP_API_KEY")

# Initialize client
client = genai.Client(api_key=API_KEY)

@st.cache_data
def explain_clause(clause_text):
    try:
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
            model="gemini-3.5-flash",
            contents=prompt
        )

        return response.text

    except Exception as e:
        return f"Error generating explanation: {str(e)}"

