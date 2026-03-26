import os
from langchain.tools import BaseTool, tool
from tavily import TavilyClient
from dotenv import load_dotenv

load_dotenv()

tavily_api_key = os.getenv("TAVILY_API_KEY")

tavily_client = TavilyClient(tavily_api_key)

@tool
def search(query: str) -> str:
    """
    Tool that searches over the internet

    Args:
        query: the query to search for
    Returns:
        The search result
    """
    
    print(f"Searching for {query}") 

    result = tavily_client.search(
    query=query,
    search_depth="advanced"
    )

    return result


TOOLS = [search]
TOOLS_BY_NAME: dict[str, BaseTool] = {tool.name: tool for tool in TOOLS}