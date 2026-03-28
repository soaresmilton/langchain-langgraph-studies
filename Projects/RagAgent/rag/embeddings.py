from dotenv import load_dotenv

from langchain_google_genai import GoogleGenerativeAIEmbeddings

load_dotenv()

def get_embeddings():
    """Retorna o modelo de embeddings do Gemini
    """

    return GoogleGenerativeAIEmbeddings(
        model="gemini-embedding-2-preview"
    )
