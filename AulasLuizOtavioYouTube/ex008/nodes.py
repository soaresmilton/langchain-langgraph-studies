from langgraph.prebuilt.tool_node import ToolNode
from langgraph.graph.state import RunnableConfig
from langgraph.runtime import Runtime

from context import Context
from state import State
from utils import load_llm
from tools import TOOLS, TOOLS_BY_NAME

tool_node =  ToolNode(tools=TOOLS)

def call_llm(state: State, runtime: Runtime[Context]) -> State:
    print('> call llm')  
    ctx = runtime.context 
    user_type = ctx.user_type
    temperature = 1 if user_type == 'plus' else 0

    print(runtime)
    print(ctx)
    print(user_type)
   
    llm_with_tools = load_llm().bind_tools(TOOLS)
    llm_wth_config = llm_with_tools.with_config(config={
        'configurable': {
            'temperature': temperature
        }
    })

    result = llm_wth_config.invoke(state['messages'])
    return {'messages': [result]}
