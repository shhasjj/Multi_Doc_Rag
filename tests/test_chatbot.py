from utils.chatbot import chat

query = "What are Large Language Models?"

result = chat(query)

print("=" * 80)
print("QUESTION")
print(query)

print("\n" + "=" * 80)
print("ANSWER")
print(result["answer"])

print("\n" + "=" * 80)
print("DOCUMENTS USED")

for doc in result["documents"]:
    print(doc.metadata)