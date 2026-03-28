from typing import List
from langchain_core.messages import HumanMessage, SystemMessage, BaseMessage

from agent.graph import build_graph
from prompts.system_prompt import SYSTEM_PROMPT

config = {
    "configurable": {
        "thread_id": 1
    }
}

def main() -> None:
    # 1 - Inicializar graph
    graph = build_graph()

    # 2 - Definir Estado inicial do graph: --> No caso iniciando meu grafo com o system message
    messages: List[BaseMessage] = [SystemMessage(content=SYSTEM_PROMPT)]  

    while True:
        user_input = input('Pergunte ao assistente: ')
        if user_input.lower() in ['q', 'exit', 'sair']:
            break

        # 3 - Adicionar input do usuário, na lista de mensagens do estado
        messages.append(HumanMessage(content=user_input))
        
        # 4 - Executar o grafo:
        result = graph.invoke(
            {
                'messages': messages
            },
            config=config
        )

        # 5 - Atualiza estado com resposta do grafo
        messages = result['messages']

        # 6 - exibir resposta
        ai_mesage = messages[-1] 
        print(f"AI: {ai_mesage.content[-1]['text']}") 
    
if __name__ == '__main__':
    main()