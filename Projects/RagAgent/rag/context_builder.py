from typing import List
from langchain_core.documents import Document

def build_context(documents: List[Document]) -> str: 
    """
    Constrói um contexto textual a partir dos documentos recuperados.
    """

    context_parts = []
    for i, doc in enumerate(documents):
        content = doc.page_content.strip()
        source = doc.metadata.get('file_name', 'unknown')

        context_parts.append(
            f"[Source {i+1} - {source}]\n{content}"
        )

    return "\n\n".join(context_parts)

    """
    OUTPUT:

    [Source 1 - slayer.txt]
    Slayer is one of the best skills...

    [Source 2 - combat.txt]
    Combat training can be optimized by...
    """