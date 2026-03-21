import os
from dotenv import load_dotenv
from pydantic import ValidationError
from rich import print

from langchain.chat_models import init_chat_model
from langchain.tools import BaseTool, tool
from langchain_core.messages import BaseMessage
from langchain.messages import AIMessage, HumanMessage, SystemMessage, ToolMessage
from rich.markdown import Markdown

load_dotenv()

model = os.getenv('GEMINI_MODEL_3_FLASH')
llm = init_chat_model(model)

@tool
def multiply(a: float, b: float) -> float:
    """Multiply a * b and returns the result

    Args:
        a (float): multiplicand
        b (float): multiplier

    Returns:
        float: the result of the equation a * b
    """

    return a * b




system_message = SystemMessage(
    'You are a help assistant. You have access to tools. When user asks'
    'for something, first look if you have a tool that solves that problem.'
)

user_input = input("Digite sua mensagem: ")

human_message = HumanMessage(user_input)

messages: list[BaseMessage] = [system_message, human_message]

tools: list[BaseTool] = [multiply]
tools_by_name = {tool.name: tool for tool in tools}

llm_with_tools = llm.bind_tools(tools)
llm_response = llm_with_tools.invoke(messages)
messages.append(llm_response)

# Checa se a LLM chamou a tool (imagine que tem interações que nenhuma tool precisa ser chamada)
if isinstance(llm_response, AIMessage) and getattr(llm_response, 'tool_calls'):
    call = llm_response.tool_calls[-1] # pegar a última tool call
    name, args, id_ = call['name'], call['args'], call['id']
    try:
        content = tools_by_name[name].invoke(args)
        status = 'success'
    except (KeyError, IndexError, TypeError, ValidationError, ValueError) as error:
        content = f'Please, fix your mistakes: {error}'
        status = 'error'

    tool_message = ToolMessage(content=content, tool_call_id=id_, status=status)
    messages.append(tool_message)

    llm_response =  llm_with_tools.invoke(messages)
    messages.append(llm_response)

# print(Markdown(llm_response['messages'][-1].content[0]['text']))
print(messages)