from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate, load_prompt
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

import streamlit as st
load_dotenv()
model=ChatGoogleGenerativeAI(model='gemini-2.5-flash', temperature=0.9, max_output_tokens=8)

history=[
    SystemMessage(content="You are assistanat named Remo")
]

while 1:
    user_input=input("")
    history.append(HumanMessage(content=user_input))
    if user_input=="exit":
        print("Exiting chat")
        print(history)
        break
    result=model.invoke(history)
    print(result.content)
    history.append(AIMessage(content=result.content))