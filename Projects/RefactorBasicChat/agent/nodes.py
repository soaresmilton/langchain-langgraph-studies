from typing import Callable
from agent.state import AgentState
from langchain_core.messages import AIMessage

def create_llm_node(model) -> Callable[[AgentState], AgentState]:
    
    def invoke_llm(state: AgentState) -> AgentState:
        response = model.invoke(state['messages'])
        assert isinstance(response, AIMessage), "LLM não retornou AiMessage"
        return {"messages": [response]}
    
    return invoke_llm