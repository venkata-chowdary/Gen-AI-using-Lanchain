from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()

print("Starting Chat Model demo...")

model=ChatGoogleGenerativeAI(model='gemini-2.5-pro', temperature=0.1, max_output_tokens=8)
result=model.invoke("Write a quote on cricket")
print(result.content)
