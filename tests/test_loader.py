from utils.loaders import load_documents

docs = load_documents([
    "data/2024-wttc-introduction-to-ai.pdf"
])

print("Number of Documents:", len(docs))

print()

print("Metadata:")
print(docs[0].metadata)

print()

print("First 300 Characters:")
print(docs[0].page_content[:300])