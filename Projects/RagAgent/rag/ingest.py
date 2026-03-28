# prepara os dados: carrega arquivos, faz chunking, gera embeddings, salva vector store

from rag.loader import load_txt_files
from rag.chunking import split_documents
from rag.vectorstore import create_vectorstore

BASE_PATH="C:/Users/Administrador/OneDrive/Documentos/Projects/006_langraph_langchain/Projects/RagAgent/data/raw"
PERSIST_PATH="C:/Users/Administrador/OneDrive/Documentos/Projects/006_langraph_langchain/Projects/RagAgent/data/vectorstore"

def run_ingestion(
        data_path: str = BASE_PATH,
        persist_path: str = PERSIST_PATH
):
    """Executa o pipeline de ingestão
    """

    print("Loading documents...")
    docs = load_txt_files(data_path)
    print(f"Loaded {len(docs)} documents.")

    print("Splitting documents...")
    chunks = split_documents(docs)
    print(f"Generated {len(chunks)} chunks.")

    print("Creating vector store...")
    vectorstore = create_vectorstore(chunks)
    
    print("Saving vector store...")
    vectorstore.save_local(persist_path)


if __name__ == "__main__":
    run_ingestion()