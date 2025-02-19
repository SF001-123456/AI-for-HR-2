from langchain_community.document_loaders import PyMuPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

def process_pdf(pdf_bytes):
    
    if pdf_bytes is None:
        return None, None

    print(f"pdf_bytes: {pdf_bytes}")
    loader = PyMuPDFLoader(pdf_bytes)

    data = loader.load()
    print(f"data: {data}")
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500, chunk_overlap=100
    )
    chunks = text_splitter.split_documents(data)

    return text_splitter, chunks
