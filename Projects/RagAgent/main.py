from google import genai
import os
from dotenv import load_dotenv
load_dotenv()

client = genai.Client()

result = client.models.embed_content(
    model="gemini-embedding-001",
    contents="Qual sentido da vida?"
)

print(result.embeddings)