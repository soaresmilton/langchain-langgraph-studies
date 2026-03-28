from typing import List

from langchain_core.documents import Document
from langchain_community.vectorstores import FAISS
from langchain_core.vectorstores import VectorStore

from rag.embeddings import get_embeddings
from rag.loader import load_txt_files
from rag.chunking import split_documents

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

docs = load_txt_files("C:/Users/Administrador/OneDrive/Documentos/Projects/006_langraph_langchain/Projects/RagAgent/data/raw")
chunks = split_documents(docs)
vs = create_vectorstore(chunks)

res = vs.similarity_search("Qual quest precisa de lvl 70 de hunter como requisito?")

print(res[0].metadata['file_name'])
