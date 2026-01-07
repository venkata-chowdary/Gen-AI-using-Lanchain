from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

load_dotenv()

print("Starting Chat Model demo...")

model=ChatGoogleGenerativeAI(model='gemini-2.5-flash', temperature=0.9)

parser=JsonOutputParser()
template=PromptTemplate(
    template= "Give me the name age of a fictioanl person {format_instructions}",
    input_variables=[],
    partial_variables={
        "format_instructions": parser.get_format_instructions()
    }
)
# prompt=template.format()
# result=model.invoke(prompt)
# parsed_op=parser.parse(result.content)
# print(parsed_op)


#using chain
chain = template | model | parser
result=chain.invoke({})
print(result)