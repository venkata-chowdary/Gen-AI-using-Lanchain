from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel, RunnableSequence, RunnablePassthrough,RunnableLambda

load_dotenv()

print("Starting Chat Model demo...")
def word_counter(text_dict):
    text = text_dict["joke"]
    return len(text.split())

model = ChatGoogleGenerativeAI(
    model="gemini-3-flash-preview",
    temperature=0.9
)

parser = StrOutputParser()

p1 = PromptTemplate(
    template="Generate a joke about {topic} in 10 words",
    input_variables=["topic"]
)

joke_chain = RunnableSequence(p1 | model | parser)

result = joke_chain.invoke({"topic": "cricket"})
print("Generated Joke:", result)
joke = result

final_chain = RunnableParallel({
    "joke": RunnablePassthrough(),   
    "counter": RunnableLambda(word_counter),
})

final_result = final_chain.invoke({"joke": joke})

print(final_result)
