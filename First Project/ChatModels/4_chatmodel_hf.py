from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from dotenv import load_dotenv
load_dotenv()
llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Meta-Llama-3-8B-Instruct",
    task="conversational",   # use chat/conversational instead
)

chat = ChatHuggingFace(llm=llm)
result = chat.invoke("What is the capital of India?")
print(result.content)
