from langchain_google_genai import GoogleGenerativeAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

llm = GoogleGenerativeAI(model="gemini-2.5-flash")

prompt = PromptTemplate(
    input_variables=["topic"],
    template="Write 5 points about {topic}."
)

chain = LLMChain(llm=llm, prompt=prompt)
print(chain.run("Artificial Intelligence"))
