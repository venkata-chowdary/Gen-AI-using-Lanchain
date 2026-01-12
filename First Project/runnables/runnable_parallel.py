from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel, RunnableSequence

load_dotenv()

print("Starting Chat Model demo...")

model = ChatGoogleGenerativeAI(
    model="gemini-3-flash-preview",
    temperature=0.9
)

parser = StrOutputParser()

p1=PromptTemplate(
    template="Generate a short simple report about {topic}",
    input_variables=["topic"]
)

p2=PromptTemplate(
    template="Generate 5 quiz questions on {topic}",
    input_variables=["topic"]
)

p3=PromptTemplate(
    template="Using this report: {notes} and these questions: {questions} Generate a single document",
    input_variables=["notes", "questions"]
)

parallel_chain=RunnableParallel({
    "notes": RunnableSequence(p1, model, parser),
    "questions": RunnableSequence(p2, model, parser)
})

result = parallel_chain.invoke({"topic": "cricket"})
print(result)