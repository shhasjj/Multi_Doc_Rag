from utils.embeddings import load_embedding_model
from utils.vectorstore import load_vector_store


def retrieve_context(query, k=3):
    """
    Retrieve the top-k most relevant document chunks.
    """

    embeddings = load_embedding_model()

    vector_store = load_vector_store(embeddings)

    retriever = vector_store.as_retriever(
        search_kwargs={"k": k}
    )

    docs = retriever.invoke(query)

    context = "\n\n".join(
        [doc.page_content for doc in docs]
    )

    return context, docs