import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from rich import print

load_dotenv()

model_type = os.getenv("GEMINI_MODEL")

model = init_chat_model(model_type)

response =  model.invoke("Olá LLM! Como vc vai?")

print(response)