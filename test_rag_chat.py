from app.chat.rag_chat import rag_chat

questions = [
    "What is photosynthesis?",
    "Define respiration",
    "What is the chemical formula of water?",
    "Explain Newton's first law"
]

for q in questions:
    print("=" * 80)
    print("Question:", q)
    response = rag_chat(q)
    print("Answer:\n", response["answer"])
