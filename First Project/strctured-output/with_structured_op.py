from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from typing import TypedDict, Annotated
load_dotenv()

print("Starting Chat Model demo...")

review="""I recently upgraded to the Samsung Galaxy S24 Ultra, and I must say, it’s an absolute powerhouse! The Snapdragon 8 Gen 3 processor makes everything lightning fast—whether I’m gaming, multitasking, or editing photos. The 5000mAh battery easily lasts a full day even with heavy use, and the 45W fast charging is a lifesaver.

However, the weight and size make it a bit uncomfortable for one-handed use. Also, Samsung’s One UI still comes with bloatware—why do I need five different Samsung apps for things Google already provides? The $1,300 price tag is also a hard pill to swallow.

Pros:
Insanely powerful processor (great for gaming and productivity)
Stunning 200MP camera with incredible zoom capabilities
Long battery life with fast charging

"""

class Review(TypedDict):
    summary: Annotated['str', "A brief summary of the review in 8 words or less."]
    sentiment: Annotated['str', "The overall sentiment of the review: Positive, Negative, or Neutral."] 
    negatives : Annotated[list['str'], "A list of positives aspects of the product."]
    

model=ChatGoogleGenerativeAI(model='gemini-2.5-flash', temperature=0.9)
str_model=model.with_structured_output(Review)
result=str_model.invoke(review)

print(result)
