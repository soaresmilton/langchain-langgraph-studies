from typing import List
from langchain_core.documents import Document
from langchain_core.vectorstores import VectorStore, VectorStoreRetriever

def get_retriever(vectorstore: VectorStore) -> VectorStoreRetriever:
    """Cria um retriever a partir do vector store

    Args:
        vectorstore (VectorStore): _description_
    """
    
    return vectorstore.as_retriever(
        search_type="similarity",
        search_kwargs={
            "k": 4
        }
    )

def retrieve_documents(retriever, query: str) -> List[Document]:
    """Executa a busca semantica
    """

    docs =  retriever.invoke(query)
    return docs