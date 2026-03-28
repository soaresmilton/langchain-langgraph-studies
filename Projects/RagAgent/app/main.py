# usa os dados, recebe pergunta, chama retriever, chama LLM, responde
from langchain_core.messages import HumanMessage
from langchain_core.language_models.chat_models import BaseChatModel

from rag.vectorstore import load_vectorstore
from rag.retriever import get_retriever, retrieve_documents
from rag.context_builder import build_context
from llm.factory import get_model
from prompts.system_prompt import build_prompt



BASE_PATH="C:/Users/Administrador/OneDrive/Documentos/Projects/006_langraph_langchain/Projects/RagAgent/data/raw"
PERSIST_PATH="C:/Users/Administrador/OneDrive/Documentos/Projects/006_langraph_langchain/Projects/RagAgent/data/vectorstore"


def main():
    # 1 - Carregar vector store (já processado)
    vectorstore = load_vectorstore(PERSIST_PATH)

    # 2 - Criar retriever
    retriever = get_retriever(vectorstore=vectorstore)

    # 3 - LLM
    model: BaseChatModel = get_model()
    print("OSRS RAG Advisor iniciado! Digite 'exit' para sair.\n")

    while True:
        question = input("Pergunte ao seu conselheiro OSRS: ")
        if question.lower() in ['exit', 'q', 'sair']:
            break

        # 4 - Buscar documentos relevantes
        retrieved_docs = retrieve_documents(retriever, question)

        # 5 - Construir o contexto com os chunks retornados pelo retriever
        context = build_context(retrieved_docs)

        # DEBUG: 
        #print("\n[DEBUG] Retrieved Context:\n")
        #print(context[:500])  # mostra só parte
        #print("\n" + "=" * 50)

        # 6 - Construir prompt:
        prompt = build_prompt(context, question)

        # 7 - Chama a LLM
        response = model.invoke([HumanMessage(content=prompt)])

        print("\nAI:")
        print(response.content[0]['text'])
        print("\n" + "-" * 50 + "\n")


if __name__ == "__main__":
    main()