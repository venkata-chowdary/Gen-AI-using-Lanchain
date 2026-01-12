from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

load_dotenv()

print("Starting Chat Model demo...")

parser = JsonOutputParser()

prompt = PromptTemplate(
    template="""
Generate 5 interesting facts about {topic} in the following JSON format:

{{
  "facts": [
    "fact 1",
    "fact 2",
    "fact 3",
    "fact 4",
    "fact 5"
  ]
}}

Ensure the output is ONLY valid JSON.
""",
    input_variables=["topic"]
)

model = ChatGoogleGenerativeAI(
    model="gemini-3-flash-preview",
    temperature=0.9
)

chain = prompt | model | parser

result = chain.invoke({"topic": "cricket"})

chain.get_graph().print_ascii()
print(result)
