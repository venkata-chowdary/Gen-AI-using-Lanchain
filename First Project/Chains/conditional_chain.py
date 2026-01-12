from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.runnables import RunnableMap, RunnableLambda
from langchain_core.prompts import PromptTemplate

load_dotenv()

print("Starting Chat Model demo...")

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.9
)

# Structured output schema
output_schema ={
    "title": "Feedback Analysis",
    "type": "object",
    "properties": {
        "summary": {"type":"string", "description": "a brief summary of the feedback"},
        "sentiment": {"type":"string", "enum": ["positive", "negative"], "description": "the overall sentiment"}
    }
}

model_with_structured_output = model.with_structured_output(output_schema)

# Feedback input
feedback = """I hate the new features in the latest update, especially the improved user interface. However, the app crashes occasionally which is quite frustrating. so what's the use of new features if the app is not stable? Overall, I think it's a step in the right direction but needs some fixes."""

# Analyze feedback
result = model_with_structured_output.invoke(feedback)
sentiment = result['sentiment']  # access as dict key
feedback_analysis = result
# Prompts
p_positive = PromptTemplate(
    template="Write an appropriate response to positive feedback for {feedback_analysis}",
    input_variables=["feedback_analysis"]
)

p_negative = PromptTemplate(
    template="Write an appropriate response to negative feedback for {feedback_analysis}",
    input_variables=["feedback_analysis"]
)

# RunnableMap for positive/negative
conditional_chain = RunnableMap({
    "positive": p_positive | model,
    "negative": p_negative | model,
})

# RunnableLambda to select branch based on sentiment
select_branch = RunnableLambda(lambda x: x['sentiment'] if isinstance(x, dict) else x)

# Full chain
full_chain = select_branch | conditional_chain

# Invoke
response = full_chain.invoke({"sentiment": sentiment})

print("Feedback Sentiment:", sentiment)
print("Response to Feedback:", response)
