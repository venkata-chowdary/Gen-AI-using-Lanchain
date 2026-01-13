from langchain_community.document_loaders import WebBaseLoader

loader = WebBaseLoader("https://en.wikipedia.org/wiki/Cricket")
docs = loader.load()
for doc in docs:
    print(doc.page_content)
    print("----- End of Document -----")    