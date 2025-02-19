from langchain_community.vectorstores import Chroma
from langchain_ollama import OllamaEmbeddings

def create_vector_store(chunks, persist_directory="./chroma_db"):
    embeddings = OllamaEmbeddings(model="deepseek-r1")
    vectorstore = Chroma.from_documents(
        documents=chunks, embedding=embeddings, persist_directory=persist_directory
    )
    retriever = vectorstore.as_retriever()
    return vectorstore, retriever
