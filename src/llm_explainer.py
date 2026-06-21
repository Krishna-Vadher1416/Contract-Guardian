# src/llm_explainer.py

import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Get API Key
API_KEY = os.getenv("GOOGLE_API_KEY")

# Configure Gemini
genai.configure(api_key=API_KEY)


def explain_clause(clause_text):
    """
    Explains a legal clause using Gemini AI.
    Returns simplified explanation + risk level + reason.
    """

    # Safety check
    if not clause_text or clause_text.strip() == "":
        return "No clause text provided."

    try:
        model = genai.GenerativeModel("gemini-pro")

        prompt = f"""
You are a legal AI assistant.

Explain the following contract clause in simple English.

Also provide:
1. Risk Level (Low / Medium / High)
2. Reason for the risk

Clause:
{clause_text}
"""

        response = model.generate_content(prompt)

        return response.text if response.text else "No response generated."

    except Exception as e:
        return f"Error generating explanation: {str(e)}"