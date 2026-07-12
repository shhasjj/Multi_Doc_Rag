import os
import streamlit as st
from dotenv import load_dotenv
from google import genai

# Load local .env (for local development)
load_dotenv()

# Streamlit Secrets → Local .env
API_KEY = st.secrets.get(
    "GOOGLE_API_KEY",
    os.getenv("GOOGLE_API_KEY")
)

if not API_KEY:
    raise ValueError("GOOGLE_API_KEY is missing.")

client = genai.Client(
    api_key=API_KEY
)


def ask_llm(prompt):
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text