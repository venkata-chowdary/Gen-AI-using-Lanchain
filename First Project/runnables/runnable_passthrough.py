from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel, RunnableSequence, RunnablePassthrough

load_dotenv()

print("Starting Chat Model demo...")

model = ChatGoogleGenerativeAI(
    model="gemini-3-flash-preview",
    temperature=0.9
)

parser = StrOutputParser()

p1 = PromptTemplate(
    template="Generate a joke about {topic}",
    input_variables=["topic"]
)

p2 = PromptTemplate(
    template="Explain this joke: {joke}",
    input_variables=["joke"]
)

joke_chain = RunnableSequence(p1 | model | parser)

result = joke_chain.invoke({"topic": "cricket"})
joke = result

final_chain = RunnableParallel({
    "joke": RunnablePassthrough(),   # passes {"joke": ...}
    "explanation": p2 | model | parser
})

final_result = final_chain.invoke({"joke": joke})

print(final_result)
