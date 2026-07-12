from utils.retriever import retrieve_context

query = "What is decoder"

context, docs = retrieve_context(query)

print("=" * 80)
print("Retrieved Context:\n")
print(context)

print("\n" + "=" * 80)
print("Number of Retrieved Documents:", len(docs))