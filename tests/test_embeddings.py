from utils.embeddings import load_embedding_model

embeddings = load_embedding_model()

vector = embeddings.embed_query(
    "What is a transformer?"
)

print(type(vector))
print(len(vector))
print(vector[:10])