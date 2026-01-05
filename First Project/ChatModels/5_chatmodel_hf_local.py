from langchain_huggingface import ChatHuggingFace
from langchain_huggingface import HuggingFacePipeline
import os

os.environ["HF_HOME"]='D:/GenAI/hf_cache'  # Set the Hugging Face cache directory

llm = HuggingFacePipeline.from_model_id(
    model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
    pipeline_kwargs={"temperature": 0.7, "max_new_tokens": 256}
)

model=ChatHuggingFace(llm=llm)

result=model.invoke("What is the capital of India?")
print(result)