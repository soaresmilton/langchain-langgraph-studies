from dotenv import load_dotenv
from rich import print
from langchain.agents import create_agent
from langchain.messages import HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from state import State
from tools import TOOLS
from response_format import ListResponseStructure

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-3-flash-preview",
    temperature=1
)

agent = create_agent(model=llm, tools=TOOLS, response_format=ListResponseStructure)

def main() -> None:
    human_message = HumanMessage(input("Faça sua pesquisa: "))

    state = State(messages=human_message)

    result = agent.invoke(state)
    print(result['structured_response'])

if __name__ == '__main__':
    main()
