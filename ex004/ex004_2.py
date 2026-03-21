import os
import threading
from dotenv import load_dotenv
from typing import Annotated, TypedDict, Sequence
from rich import print
from rich.markdown import Markdown
from langchain.chat_models import init_chat_model
from langchain.messages import AIMessage, HumanMessage
from langgraph.graph import END, START, StateGraph, add_messages
from langgraph.checkpoint.memory import InMemorySaver
from langchain_core.messages import BaseMessage
from langgraph.graph.state import RunnableConfig


load_dotenv()

model_type = os.getenv("GEMINI_MODEL")

model = init_chat_model(model_type)

# 1 - definir state
class AgentState(TypedDict):
    messages: Annotated[Sequence[BaseMessage], add_messages]

# 2 - definir nodes
def call_llm(state: AgentState) -> AgentState:
    model_result = model.invoke(state['messages'])
    return {'messages': [model_result]} 

# 3 - criar StateGraph
builder = StateGraph(AgentState, context_schema=None, input_schema=AgentState, output_schema=AgentState)

# 4 - adicionar nodes ao grafo
builder.add_node('call_llm', call_llm)
builder.add_edge(START, 'call_llm')
builder.add_edge('call_llm', END)

# 5 - compilar o grapho
checkpointer = InMemorySaver()
graph = builder.compile(checkpointer=checkpointer)

# Configuração para o agente memorizar a conversa
config = RunnableConfig(
    {
        'configurable': {
            'thread_id': threading.get_ident()
        }
    }
)

# 6 - Usar o grapho 
if __name__ == '__main__':
    while True:
        user_input = input('Digite sua mensagem: ')
        print(Markdown('---'))
        
        if user_input.lower() in ['exit', 'q', 'sair']:
            break

        human_message = HumanMessage(user_input)
        
        result  = graph.invoke({'messages': [human_message]}, config=config)

        print(Markdown(result['messages'][-1].content[0]['text']))
        print(Markdown('---'))
