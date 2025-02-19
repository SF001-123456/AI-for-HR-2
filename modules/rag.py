from .llm import ollama_llm

def combine_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

def rag_chain(question, retriever):
    retrieved_docs = retriever.invoke(question)
    formatted_content = combine_docs(retrieved_docs)
    print("formatted_content: ", formatted_content)

    return ollama_llm(question, formatted_content)
