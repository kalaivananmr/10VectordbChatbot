from app.ingest.loader import load_pdf
from app.ingest.validator import validate_docs
from app.ingest.splitter import split_docs

PDF_PATH = r"D:\sslc-science-chatbot\data\sslc_science.pdf"

docs = validate_docs(load_pdf(PDF_PATH))
chunks = split_docs(docs)

print("Total chunks:", len(chunks))
print("Sample chunk:\n")
print(chunks[0].page_content[:400])