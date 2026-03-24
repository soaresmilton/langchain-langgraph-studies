from langgraph.graph.state import CompiledStateGraph, StateGraph
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.constants import END, START
from langgraph.prebuilt import tools_condition

from state import State
from nodes import call_llm, tool_node

checkpointer = InMemorySaver()

def build_graph() -> CompiledStateGraph[State, None, State, State]:
    builder = StateGraph(State)

    builder.add_node('call_llm', call_llm)
    builder.add_node('tools', tool_node)        

    builder.add_edge(START, 'call_llm')
    builder.add_conditional_edges('call_llm', tools_condition, ['tools', END])
    builder.add_edge('tools', 'call_llm')

    builder.add_edge('call_llm', END)

    return builder.compile(checkpointer=checkpointer)