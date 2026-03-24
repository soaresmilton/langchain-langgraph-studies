from typing import Literal

from langchain.messages import AIMessage, ToolMessage
from langgraph.graph.state import CompiledStateGraph, StateGraph
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.constants import END, START
from langchain_core.runnables.config import RunnableConfig
from pydantic import ValidationError

from tools import TOOLS, TOOLS_BY_NAME
from state import State
from utils import load_llm

from rich import print

checkpointer = InMemorySaver()

def call_llm(state: State, config: RunnableConfig) -> State:
    print('> call llm')   
    # user_type = config['configurable']['user_type']
    user_type = config.get('configurable', {}).get('user_type')
    temperature = 1 if user_type == 'plus' else 0
   

    llm_with_tools = load_llm().bind_tools(TOOLS)
    llm_wth_config = llm_with_tools.with_config(config={
        'configurable': {
            'temperature': temperature
        }
    })

    result = llm_wth_config.invoke(state['messages'])
    return {'messages': [result]}

def tool_node(state: State) -> State:
    print('> tool node')
    llm_response = state['messages'][-1]

    if not isinstance(llm_response, AIMessage) or not getattr(llm_response, 'tool_calls', None):
        return state
    
    call = llm_response.tool_calls[-1]
    name, args, id_ = call['name'], call['args'], call['id']

    try:
        content = TOOLS_BY_NAME[name].invoke(args)
        status = "success"
    except (KeyError, IndexError, TypeError, ValidationError, ValueError) as error:
        content = f"Fix your mistakes: {error}"
        status = "error"

    tool_message = ToolMessage(content=content, tool_call_id = id_, status=status)
    return {"messages": [tool_message]}

def router(state: State) -> Literal["tool_node", '__end__']:
    print('> router')
    llm_response  = state["messages"][-1]
    if getattr(llm_response, 'tool_calls'):
        return "tool_node"
    return "__end__"
    

def build_graph() -> CompiledStateGraph[State, None, State, State]:
    builder = StateGraph(State)

    builder.add_node('call_llm', call_llm)
    builder.add_node('tool_node', tool_node)        

    builder.add_edge(START, 'call_llm')
    builder.add_conditional_edges('call_llm', router, ['tool_node', '__end__'])
    builder.add_edge('tool_node', 'call_llm')

    builder.add_edge('call_llm', END)

    return builder.compile(checkpointer=checkpointer)