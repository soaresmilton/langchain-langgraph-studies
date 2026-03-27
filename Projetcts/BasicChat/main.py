from dotenv import load_dotenv
from typing import List
from langchain_core.messages import HumanMessage, SystemMessage, BaseMessage

from prompts import SYSTEM_PROMPT
from graph import build_graph
from runnable_config import runnable_config

def main() -> None:
    graph = build_graph()
    all_messages: List[BaseMessage] = []
    system_message = SystemMessage(content=SYSTEM_PROMPT)
    llm_config = runnable_config

    while True:
        input_prompt = input("Fale com o assistente: ")

        if input_prompt.lower() in ["q", "exit"]:
            break
        
        human_input = HumanMessage(content=input_prompt)

        current_loop_messages = [system_message, human_input]

        result = graph.invoke({"messages": current_loop_messages}, config=llm_config)

        print(result['messages'][-1].content[0]['text'])

        all_messages = result['messages']
    
    print (all_messages)

if __name__ == "__main__":
    main()