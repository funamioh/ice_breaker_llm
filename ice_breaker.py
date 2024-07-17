from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain.chains import LLMChain

information ="""
Willard Carroll Smith II[3] (born September 25, 1968) is an American actor, rapper and film producer. He has received multiple accolades, including an Academy Award, a Golden Globe Award, a BAFTA Award, and four Grammy Awards.[4][5][6] As of 2024, his films have grossed over $9.3 billion globally,[7] making him one of Hollywood's most bankable stars.[8][9]

Smith began his acting career starring as a fictionalized version of himself on the NBC sitcom The Fresh Prince of Bel-Air (1990–1996), for which he was nominated for the Golden Globe Award for Best Actor – Television Series Musical or Comedy in 1993 and 1994. He first gained recognition as part of a hip hop duo with DJ Jazzy Jeff, with whom he released five studio albums which contained five Billboard Hot 100-top 20 singles—"Parents Just Don't Understand", "A Nightmare on My Street", "Summertime", "Ring My Bell", and "Boom! Shake the Room"—from 1984 to 1994. He released the solo albums Big Willie Style (1997), Willennium (1999), Born to Reign (2002), and Lost and Found (2005), which spawned the US number-one singles "Gettin' Jiggy wit It" and "Wild Wild West" (featuring Dru Hill and Kool Moe Dee). He has won four Grammy Awards for his recording career.[10]
"""

if __name__ == "__main__":
    print("Hello LangChain!")

    summary_template = """
    given the information about a person from I want you to create:
    1. a short summary
    2. two interesting facts about them
    """

    summary_prompt_template = PromptTemplate(input_variable="information", template=summary_template)

    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

    chain = summary_prompt_template | llm
    res = chain.invoke(input={"information": information})

    print(res)