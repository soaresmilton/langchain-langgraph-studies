import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from rich import print

load_dotenv()

google_api_key = os.getenv("GOOGLE_API_KEY")

model = init_chat_model('google_genai:gemini-3-flash-preview')

response =  model.invoke("Olá LLM! Como vc vai?")

print(response)