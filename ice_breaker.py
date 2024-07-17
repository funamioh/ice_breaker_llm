from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_community.chat_models import ChatOllama

# from langchain.chains import LLMChain

if __name__ == "__main__":
    load_dotenv()
    print("Hello LangChain!")
    information = """
        Willard Carroll Smith II[3] (born September 25, 1968) is an American actor, rapper and film producer. He has 
    received multiple accolades, including an Academy Award, a Golden Globe Award, a BAFTA Award, and four Grammy 
    Awards.[4][5][6] As of 2024, his films have grossed over $9.3 billion globally,[7] making him one of Hollywood's 
    most bankable stars.[8][9]
    """

    summary_template = """
    Write me a song
    """

    summary_prompt_template = PromptTemplate(
        input_variable="information", template=summary_template
    )

    # llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")
    llm = ChatOllama(model="mistral")

    chain = summary_prompt_template | llm | StrOutputParser()
    res = chain.invoke(input={"information": information})

    print(res)
