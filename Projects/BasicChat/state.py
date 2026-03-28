from langgraph.graph.message import BaseMessage, add_messages
from typing import TypedDict, Annotated
from collections.abc import Sequence

class AgentState(TypedDict):
    messages: Annotated[Sequence[BaseMessage], add_messages] 