from email.encoders import encode_noop
from importlib import metadata
from pathlib import Path
from typing import List

from langchain_core.documents import Document

def load_txt_files(data_path: str) -> List[Document]:
    """
        Carrega todos os arquivos .txt de um diretório e retorna como lista de Document
    """

    base_path = Path(data_path)
    if not base_path.exists():
        raise ValueError(f"Path does not exist: {data_path}")
    
    documents: List[Document] = []

    for file_path in base_path.glob("*.txt"):
        content =  file_path.read_text(encoding="utf-8")

        doc = Document(
            page_content=content,
            metadata={
                "source": str(file_path),
                "file_name": file_path.name
            }
        )

        documents.append(doc)
    
    return documents