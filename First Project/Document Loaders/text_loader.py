from langchain_community.document_loaders import TextLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
load_dotenv()


loader = TextLoader("cricket.txt", encoding="utf-8")
docs=loader.load()

print("Starting Chat Model demo...")

parser = StrOutputParser()
prompt = PromptTemplate(
    template="Write a short poem on the following topic: {topic}",
    input_variables=["topic"]
)
model = ChatGoogleGenerativeAI(
    model="gemini-3-flash-preview",
    temperature=0.9
)

chain = prompt | model | parser
result = chain.invoke({"topic": docs[0].page_content})
print(result)