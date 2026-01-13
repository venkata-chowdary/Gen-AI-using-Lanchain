from langchain_community.document_loaders import PyPDFLoader

loader=PyPDFLoader("sri.pdf")
docs=loader.load()
for doc in docs:
    print(doc.page_content)
    print("----- End of Page -----")
    
