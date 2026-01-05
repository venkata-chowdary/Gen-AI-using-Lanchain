from langchain_google_genai import GoogleGenerativeAIEmbeddings 
from dotenv import load_dotenv
load_dotenv()

documents = [
    "Virat Kohli is an Indian cricketer known for his aggressive batting and leadership.",
    "MS Dhoni is a former Indian captain famous for his calm demeanor and finishing skills.",
    "Sachin Tendulkar, also known as the 'God of Cricket', holds many batting records.",
    "Rohit Sharma is known for his elegant batting and record-breaking double centuries.",
    "Jasprit Bumrah is an Indian fast bowler known for his unorthodox action and yorkers."
]

query="Tell me about virat kohli"
print("Starting Embedding Model demo...")

embeddings = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001")
query_emb= embeddings.embed_query(query)
doc_embs= embeddings.embed_documents(documents)

#use cosine similarity to find the most similar document
from sklearn.metrics.pairwise import cosine_similarity
similarities = cosine_similarity([query_emb], doc_embs)
print("Similarities:", similarities)


#these vectors can now be stored and used in a vector database for similarity search
