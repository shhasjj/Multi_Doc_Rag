from langchain_community.vectorstores import FAISS

DB_PATH = "faiss_index"


def create_vector_store(chunks, embeddings):
    """
    Create and save FAISS vector store.
    """
    vector_store = FAISS.from_documents(
        documents=chunks,
        embedding=embeddings
    )

    vector_store.save_local(DB_PATH)

    return vector_store


def load_vector_store(embeddings):
    """
    Load existing FAISS vector store.
    """
    return FAISS.load_local(
        DB_PATH,
        embeddings,
        allow_dangerous_deserialization=True
    )