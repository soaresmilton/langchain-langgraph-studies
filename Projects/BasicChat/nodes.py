from dotenv import load_dotenv
from state import AgentState
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import create_agent

load_dotenv()

def invoke_llm(state: AgentState) -> AgentState:
    model = ChatGoogleGenerativeAI(
        model="gemini-3-flash-preview",
        temperature=0
    )

    agent = create_agent(model=model)
    return agent.invoke(state)