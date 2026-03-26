import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from langchain_core.prompts import PromptTemplate
from rich import print

load_dotenv()

def main():
    model = ChatGoogleGenerativeAI(
        model="gemini-3-flash-preview",
        temperature=0
    )

    information = """
    Old School RuneScape is a massively multiplayer online role-playing game (MMORPG), developed and published by Jagex. The game was released on 16 February 2013. When Old School RuneScape launched, it began as an August 2007 version of the game RuneScape, which was highly popular prior to the launch of RuneScape 3. The game has since received engine improvements, new content, and quality of life updates largely decided by the community via in-game polls. Despite originally having a smaller development team and a slower update schedule relative to RuneScape, Old School RuneScape is now the more popular version of the game, with an all-time record of over 240,000 concurrent players in August 2025.[1][2] A mobile version for Android and iOS was released in October 2018.[3]
    """
    summary_template ="""
    given the information {information} about a game I want you to create:

    1. A short summary
    2. two interesting facts about them
    3. answers always in Portuguese (Brazil)
    """

    summary_prompt_template = PromptTemplate(
        input_variables=['information'], template=summary_template
    )

    chain = summary_prompt_template | model
    response = chain.invoke({"information": information})
    print(response)

if __name__ == '__main__':
    main()