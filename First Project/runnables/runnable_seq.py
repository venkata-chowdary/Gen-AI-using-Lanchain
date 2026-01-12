from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence

load_dotenv()

print("Starting Chat Model demo...")
model=ChatGoogleGenerativeAI(model='gemini-3-flash-preview', temperature=0.9)

prompt=PromptTemplate(
    template="write a joke about {topic}",
    input_variables=["topic"],
)
parser=StrOutputParser()

chain=RunnableSequence(prompt, model, parser)
print(chain.invoke({"topic": "Cricket"}))