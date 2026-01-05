from langchain_google_genai import GoogleGenerativeAIEmbeddings 
from dotenv import load_dotenv
load_dotenv()

print("Starting Embedding Model demo...")

embeddings = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001")
vector = embeddings.embed_query("hello, world!")
print(vector)