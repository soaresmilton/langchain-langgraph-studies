from typing import List
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter

from rag.loader import load_txt_files

def split_documents(
        documents: List[Document],
        chunk_size: int = 500,
        chunk_overlap: int = 100
) -> List[Document]:
    """Divide documentos em chunks menores mantendo o contexto

    Args:
        documents (List[Document]): _description_
        chunk_size (int, optional): _description_. Defaults to 500.
        chunk_overlap (int, optional): _description_. Defaults to 100.

    Returns:
        List[Document]: _description_
    """

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )

    chunks = splitter.split_documents(documents)

    return chunks