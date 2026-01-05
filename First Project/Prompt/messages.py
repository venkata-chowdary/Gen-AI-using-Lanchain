from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv

load_dotenv()
model=ChatGoogleGenerativeAI(model='gemini-2.5-flash', temperature=0.9, max_output_tokens=8)

messages=[
    SystemMessage(content="You are assistanat named Remo"),
    HumanMessage(content="Hello, who are you?")
]

result=model.invoke(messages)
messages.append(AIMessage(content=result.content))
print(messages)


