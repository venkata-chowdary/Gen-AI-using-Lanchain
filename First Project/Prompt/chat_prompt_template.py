from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
load_dotenv()

domain="Telugu Movies"
user_query="Recommend me some good movies to watch of Jr NTR"
chat_template=ChatPromptTemplate([
    SystemMessage(content='You are a remo a friendly and helpful assistant expert in {domain}.'),
    HumanMessage(content='{user_query}'),
])

model=ChatGoogleGenerativeAI(model='gemini-2.5-flash', temperature=0.9, max_output_tokens=8)
prompt=chat_template.invoke({
    "domain":domain,
    "user_query":user_query
})

result = model.invoke(prompt)
print("_____________________________")
print(result)