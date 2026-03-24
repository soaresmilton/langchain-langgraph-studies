from langgraph.prebuilt.tool_node import ToolNode
from langgraph.graph.state import RunnableConfig

from state import State
from utils import load_llm
from tools import TOOLS, TOOLS_BY_NAME

tool_node =  ToolNode(tools=TOOLS)

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
