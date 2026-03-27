from langgraph.graph import START, END
from langgraph.graph.state import CompiledStateGraph, StateGraph
from langgraph.checkpoint.memory import InMemorySaver

from nodes import invoke_llm
from state import AgentState

checkpointer = InMemorySaver()

def build_graph() -> CompiledStateGraph[AgentState, None, AgentState, AgentState]:
    builder = StateGraph(AgentState)

    builder.add_node('invoke_llm', invoke_llm)

    builder.add_edge(START, 'invoke_llm')
    builder.add_edge('invoke_llm', END)

    return builder.compile(checkpointer=checkpointer)