from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field

load_dotenv()

print("Starting Chat Model demo...")

model=ChatGoogleGenerativeAI(model='gemini-2.5-flash', temperature=0.9)


class Person(BaseModel):
    name: str =Field(..., description="name of the person")
    age: int = Field(..., description="age of the person")
    city: str = Field(..., description="city of the person belongs to") 
    
parser=PydanticOutputParser(pydantic_object=Person)
template=PromptTemplate(
    template= "Give me the name, age and city of a fictioanl person {format_instructions}",
    input_variables=[],
    partial_variables={
        "format_instructions": parser.get_format_instructions()
    }
) 

prompt=template.invoke({})
result=model.invoke(prompt)
print(prompt)
print(parser.parse(result.content))