from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.runnables import RunnableParallel

load_dotenv()

print("Starting Chat Model demo...")

model = ChatGoogleGenerativeAI(
    model="gemini-3-flash-preview",
    temperature=0.9
)

parser = JsonOutputParser()

# PROMPT 1
prompt_1 = PromptTemplate.from_template("""
Generate a short simple report about {topic} in the following JSON:

{{
  "report": ""
}}

ONLY return valid JSON.
""")

# PROMPT 2
prompt_2 = PromptTemplate.from_template("""
Generate 5 short questions about {topic} in the following JSON:

{{
  "questions": [
    "q1",
    "q2",
    "q3",
    "q4",
    "q5"
  ]
}}

ONLY return valid JSON.
""")

# PROMPT 3
prompt_3 = PromptTemplate.from_template("""
merge this {notes} and these {questions} into a single document:
Generate this JSON:

{{
  "document": ""
}}

ONLY return valid JSON.
""")

parallel_chain = RunnableParallel({
    "notes": prompt_1 | model | parser,
    "questions": prompt_2 | model | parser
})

merge_chain = prompt_3 | model | parser

chain = parallel_chain | merge_chain

result = chain.invoke({"topic": "cricket"})
chain.get_graph().print_ascii()
print(result)
