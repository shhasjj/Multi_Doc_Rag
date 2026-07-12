import os
from pathlib import Path
from dotenv import load_dotenv
from google import genai

# Project root
BASE_DIR = Path(__file__).resolve().parent.parent

# Absolute path to .env
ENV_PATH = BASE_DIR / ".env"

# Load .env
load_dotenv(dotenv_path=ENV_PATH)

api_key = os.getenv("GOOGLE_API_KEY")

if api_key is None:
    raise ValueError(f"GOOGLE_API_KEY not found in {ENV_PATH}")

client = genai.Client(api_key=api_key)


def ask_llm(prompt: str):
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )
    return response.text