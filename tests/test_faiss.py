from utils.loaders import load_documents
from utils.splitter import split_documents
from utils.embeddings import load_embedding_model
from utils.vectorstore import create_vector_store

documents = load_documents([
    "data/2024-wttc-introduction-to-ai.pdf"
])

chunks = split_documents(documents)

embeddings = load_embedding_model()

vector_store = create_vector_store(
    chunks,
    embeddings
)

print("FAISS created successfully!")

print("Total Chunks:", len(chunks))