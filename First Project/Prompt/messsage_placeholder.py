from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

load_dotenv()

# ----------------------------
# CHAT HISTORY (already formatted correctly)
# ----------------------------
chat_history = [
    HumanMessage(content="I want to request a refund for my order #12345."),
    AIMessage(content="Your refund request for order #12345 has been initiated. It will be processed in 3-5 business days.")
]

# ----------------------------
# TEMPLATE
# ----------------------------
chat_template = ChatPromptTemplate.from_messages([
    ("system", "You are Remo, a customer support agent."),
    MessagesPlaceholder(variable_name="chat_history"),
    ("human", "{query}")
])

# Fill prompt
prompt = chat_template.invoke({
    "chat_history": chat_history,
    "query": "Where is my refund? It’s been 5 days."
})

# ----------------------------
# MODEL
# ----------------------------
model = ChatGoogleGenerativeAI(
    model='gemini-2.5-flash',
    temperature=0.9,
    max_output_tokens=50
)

# Generate response
result = model.invoke(prompt.to_messages())

# ----------------------------
# OUTPUT
# ----------------------------
print(result.content)
