import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.language_models.chat_models import BaseChatModel

load_dotenv()

google_api_key = os.getenv('GOOGLE_API_KEY')

def get_model() -> BaseChatModel:

    return ChatGoogleGenerativeAI(
        model="gemini-3-flash-preview",
        temperature=0.7,
        google_api_key=google_api_key
    )