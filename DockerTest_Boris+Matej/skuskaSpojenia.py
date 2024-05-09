from langchain_openai import ChatOpenAI

llm = ChatOpenAI(api_key="sk-proj-JVr1LvP5YO4a7YFNTeApT3BlbkFJzsGbe4RSacFsSOgVSYFx")

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

inp = "Predstav sa mi"

while(inp != "0"):

    inp = input("Zadaj prompt: ")

    prompt = ChatPromptTemplate.from_messages([
                ("human", "You are helpful assistant for university students."),
                ("human", "{input}")
            ])
    

    output_parser = StrOutputParser()

    chain = prompt | llm | output_parser

    response = chain.invoke({"input": inp})


    output_parser = StrOutputParser()
    parsed_response = output_parser.parse(response)

    print(parsed_response)
    
