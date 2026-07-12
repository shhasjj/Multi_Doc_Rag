from utils.retriever import retrieve_context
from utils.llm import ask_llm


def chat(query):
    """
    Complete RAG Pipeline
    """

    # Retrieve relevant context
    context, docs = retrieve_context(query)

    prompt = f"""
You are a helpful AI assistant.

Answer ONLY using the context below.

If the answer cannot be found in the context, reply exactly:

"I couldn't find the answer in the uploaded documents."

Context:
{context}

Question:
{query}

Answer:
"""

    answer = ask_llm(prompt)

    return {
        "answer": answer,
        "documents": docs,
        "context": context
    }