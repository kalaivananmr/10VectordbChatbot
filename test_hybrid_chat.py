from app.chat.hybrid_rag_chat import hybrid_rag_chat

questions = [
    "Who is the Prime Minister of India?",
    "What is photosynthesis?"
]

for q in questions:
    print("=" * 80)
    print("Question:", q)

    # First attempt (default: no web)
    result = hybrid_rag_chat(q, allow_web=False)
    print("\nSource:", result.get("source"))
    print("Answer:", result.get("answer"))

    # Check if system is asking for permission
    if "Allow" in result.get("answer", ""):
        print("\nDo you want to allow web search?")
        print("1. Allow")
        print("2. Do Not Allow")

        while True:
            choice = input("Enter your choice (1 or 2): ").strip()
            if choice in ("1", "2"):
                break
            print("Invalid input. Please enter 1 or 2.")

        allow_web = True if choice == "1" else False

        # Second attempt with user decision
        result = hybrid_rag_chat(q, allow_web=allow_web)
        print("\nFinal Answer:")
        print("Source:", result.get("source"))
        print("Answer:", result.get("answer"))
