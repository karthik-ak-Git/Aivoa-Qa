from app.knowledge.loader import load_knowledge_base
from app.retriever.vector_store import VectorStore
docs = load_knowledge_base()
vs = VectorStore()
indexed = vs.index_documents(docs)
print(f"Indexed {indexed} documents")
results = vs.query("tablet capping defect root cause", n_results=3)
for r in results:
    score = r["score"]
    domain = r["domain"]
    content = r["content"][:100]
    print(f"  [{score:.3f}] {domain}: {content}...")
print("Vector store test passed!")
