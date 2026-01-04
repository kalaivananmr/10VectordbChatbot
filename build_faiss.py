from app.ingest.loader import load_pdf
from app.ingest.validator import validate_docs
from app.ingest.splitter import split_docs
from app.embeddings.embedder import get_embeddings
from app.vectorstore.faiss_store import build_faiss_index
import os

PDF_PATH = r"D:\sslc-science-chatbot\data\sslc_science.pdf"
VECTOR_DIR = "vector_data"

os.makedirs(VECTOR_DIR, exist_ok=True)

print("Loading PDF...")
docs = validate_docs(load_pdf(PDF_PATH))

print("Splitting text...")
chunks = split_docs(docs)
print(f"Total chunks: {len(chunks)}")

print("Creating embeddings...")
embeddings = get_embeddings()

print("Building FAISS index...")
build_faiss_index(chunks, embeddings, VECTOR_DIR)

print("FAISS index created successfully.")
