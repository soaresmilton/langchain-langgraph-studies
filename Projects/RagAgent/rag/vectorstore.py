from typing import List

from langchain_core.documents import Document
from langchain_community.vectorstores import FAISS
from langchain_core.vectorstores import VectorStore

from rag.embeddings import get_embeddings

def create_vectorstore(documents: List[Document]) -> VectorStore:
    """
    Cria um vector store FAISS a partir dos documentos.
    """

    embeddings = get_embeddings()
    vectorstore = FAISS.from_documents(
        documents=documents,
        embedding=embeddings
    )

    return vectorstore
