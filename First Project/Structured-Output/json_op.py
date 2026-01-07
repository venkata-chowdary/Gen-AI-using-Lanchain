from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate

load_dotenv()

print("Starting Chat Model demo...")

model=ChatGoogleGenerativeAI(model='gemini-2.5-pro', temperature=0.1, max_output_tokens=8)
# 1st prompt -> detailed report
template1 = PromptTemplate(
    template='Write a 10 line report on {topic}',
    input_variables=['topic']
)

# 2nd prompt -> summary
template2 = PromptTemplate(
    template='Write a 1 line summary on the following text. /n {text}',
    input_variables=['text']
)

prompt1 = template1.invoke({'topic':'black hole'})

result = model.invoke(prompt1)

prompt2 = template2.invoke({'text':result.content})

result1 = model.invoke(prompt2)

print(result1.content)
