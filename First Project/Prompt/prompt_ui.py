from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate, load_prompt

import streamlit as st
load_dotenv()

template=load_prompt('prompt_template.json')

model=ChatGoogleGenerativeAI(model='gemini-2.5-flash', temperature=0.1, max_output_tokens=8)

st.header("Research Tool")
user_input=st.text_input("Enter your prompt")
style_input = st.selectbox( "Select Explanation Style", ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"] ) 
length_input = st.selectbox( "Select Explanation Length", ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"] )

if st.button("Generate Response"):
    print("Button clicked")
    chain = template | model
    #instead of invoking twice, use chaining
    # prompt=template.invoke({
    #     "user_input": user_input,
    #     "style_input": style_input,
    #     "length_input": length_input
    # })
    
    # result=model.invoke(prompt)
    result=chain.invoke({
        "user_input": user_input,
        "style_input": style_input,
        "length_input": length_input
    })
    print("Model invoked")
    st.write(result.content)