print("APP STARTED")

import streamlit as st

from utils.file_manager import save_uploaded_files
from utils.loaders import load_documents
from utils.splitter import split_documents
from utils.embeddings import load_embedding_model
from utils.vectorstore import create_vector_store
from utils.chatbot import chat

st.set_page_config(
    page_title="Multi Document RAG",
    page_icon="📚",
    layout="wide"
)

st.title("📚 Multi Document RAG")
st.caption("Ask questions about your uploaded documents using Gemini AI.")

if "history" not in st.session_state:
    st.session_state.history = []

st.sidebar.title("📂 Upload Documents")

uploaded_files = st.sidebar.file_uploader(
    "Upload PDF, DOCX or TXT",
    type=["pdf", "docx", "txt"],
    accept_multiple_files=True
)

# -----------------------------
# Upload & Index Documents
# -----------------------------
if uploaded_files:

    file_paths = save_uploaded_files(uploaded_files)

    st.success(f"✅ {len(file_paths)} file(s) uploaded")

    documents = load_documents(file_paths)

    st.success(f"📄 Loaded {len(documents)} pages")

    chunks = split_documents(documents)

    st.success(f"🧩 Created {len(chunks)} chunks")

    embeddings = load_embedding_model()

    create_vector_store(chunks, embeddings)

    st.success("Knowledge Base Ready!")

# -----------------------------
# Ask Question
# -----------------------------
question = st.text_input("Ask a question")

if st.button("Ask"):

    if question.strip() == "":
        st.warning("Please enter a question.")

    else:

        with st.spinner("Thinking..."):

            result = chat(question)
            st.session_state.history.append(
                {
                    "question": question,
                    "answer": result["answer"]
                }
            )

        st.subheader("Answer")

        st.write(result["answer"])

        st.subheader("Documents Used")

        for doc in result["documents"]:
            st.write(doc.metadata)