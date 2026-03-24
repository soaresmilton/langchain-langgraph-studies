import os
from typing import cast
from dotenv import load_dotenv
from langchain.chat_models import BaseChatModel, init_chat_model

load_dotenv()

gemini_model = os.getenv('GEMINI_MODEL_3_FLASH')

def load_llm() -> BaseChatModel:
    base_chat_model = cast(
        'BaseChatModel', 
        init_chat_model(
            gemini_model, 
            temperature=0.2, 
            configurable_fields='any'
        )
    )

    assert hasattr(base_chat_model, 'bind_tools')
    assert hasattr(base_chat_model, 'invoke')
    assert hasattr(base_chat_model, 'with_config')
    
    return base_chat_model