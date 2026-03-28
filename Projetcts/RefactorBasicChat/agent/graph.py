# controla o meu fluxo
from langgraph.graph import StateGraph, START, END
from langgraph.graph.state import CompiledStateGraph
from langgraph.checkpoint.memory import InMemorySaver

from agent.state import AgentState
from agent.nodes import create_llm_node
from llm.factory import get_model

def build_graph() -> CompiledStateGraph[AgentState, None, AgentState, AgentState]:
    # Instanciar dependencias
    model = get_model()

    # Criando os nodes
    llm_node = create_llm_node(model)

    # Builder do grapho
    builder = StateGraph(AgentState)

    # Registrar nodes
    builder.add_node('llm_node', llm_node)

    # Definir fluxo (edges)
    builder.add_edge(START, 'llm_node')
    builder.add_edge('llm_node', END)

    # Checkpointer (memória)
    checkpointer = InMemorySaver()

    # Compilar grapho
    graph =  builder.compile(checkpointer=checkpointer)

    return graph


