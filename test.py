# verify_count.py
from app.embeddings.embedder import get_embeddings
from app.vectorstore.faiss_store import load_faiss_index

db = load_faiss_index("vector_data", get_embeddings())

# FAISS internal count
count = db.index.ntotal
print("Total vectors in FAISS:", count)

assert count > 0, "No embeddings found"
print("✓ Embedding count is non-zero")
