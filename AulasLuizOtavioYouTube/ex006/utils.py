import os
from dotenv import load_dotenv
from langchain.chat_models import BaseChatModel, init_chat_model

load_dotenv()

model = os.getenv('GEMINI_MODEL_3_FLASH')

def load_llm() -> BaseChatModel:
    return init_chat_model(model)