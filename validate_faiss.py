from app.embeddings.embedder import get_embeddings
from app.vectorstore.faiss_store import load_faiss_index

VECTOR_DIR = "vector_data"

embeddings = get_embeddings()
db = load_faiss_index(VECTOR_DIR, embeddings)

query = "What is photosynthesis?"

docs = db.similarity_search(query, k=3)

print(f"Query: {query}\n")
print(f"Retrieved {len(docs)} chunks\n")

for i, doc in enumerate(docs, 1):
    print(f"--- Chunk {i} ---")
    print(doc.page_content[:300])
    print()
