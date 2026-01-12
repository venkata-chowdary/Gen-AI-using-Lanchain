from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

load_dotenv()

print("Starting Chat Model demo...")

parser = JsonOutputParser()

prompt_1 = PromptTemplate(
    template="""
Generate detailed report about {topic} in the following JSON format:
{{
  "report": ""
}}

Ensure the output is ONLY valid JSON.
""",
    input_variables=["topic"]
)


prompt_2 = PromptTemplate(
    template="""
Generate 5 lines about {detailed_report} in the following JSON format:
{{
  "lines": [
    "line 1",
    "line 2",
    "line 3",
    "line 4",
    "line 5"
  ]
}}
Ensure the output is ONLY valid JSON.
""",
    input_variables=["detailed_report"]
)


model = ChatGoogleGenerativeAI(
    model="gemini-3-flash-preview",
    temperature=0.9
)

chain = prompt_1 | model | prompt_2 | model | parser

result = chain.invoke({"topic": "cricket"})

chain.get_graph().print_ascii()
print(result)
