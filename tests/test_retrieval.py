from utils.embeddings import load_embedding_model
from utils.vectorstore import load_vector_store

# Load embedding model
embeddings = load_embedding_model()

# Load FAISS database
vector_store = load_vector_store(embeddings)

# Create retriever
retriever = vector_store.as_retriever(
    search_kwargs={"k": 3}
)

query = "What are Transformer Decoders?"

results = retriever.invoke(query)

print(f"\nRetrieved {len(results)} chunks\n")

for i, doc in enumerate(results, start=1):
    print("=" * 70)
    print(f"Chunk {i}")
    print("Metadata:", doc.metadata)
    print()
    print(doc.page_content[:500])
    print()