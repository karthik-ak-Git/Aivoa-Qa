import chromadb
from chromadb.config import Settings as ChromaSettings
from typing import Any
from app.core.config import get_settings
from app.core.logger import get_logger

logger = get_logger("retriever.vector_store")


class VectorStore:
    """ChromaDB-backed vector store for knowledge retrieval."""

    def __init__(self):
        settings = get_settings()
        self.client = chromadb.PersistentClient(
            path=settings.VECTOR_DB_PATH,
            settings=ChromaSettings(anonymized_telemetry=False),
        )
        self.collection = self.client.get_or_create_collection(
            name=settings.VECTOR_COLLECTION_NAME,
            metadata={"hnsw:space": "cosine"},
        )
        self._is_indexed = False

    @property
    def is_indexed(self) -> bool:
        return self._is_indexed and self.collection.count() > 0

    def index_documents(self, documents: list[dict[str, Any]]) -> int:
        # Skip if already indexed in ChromaDB
        existing_count = self.collection.count()
        if existing_count > 0:
            logger.info(f"Vector store already has {existing_count} docs, skipping re-index")
            self._is_indexed = True
            return existing_count

        batch_size = 100
        total_indexed = 0

        for i in range(0, len(documents), batch_size):
            batch = documents[i:i + batch_size]
            ids = [doc["id"] for doc in batch]
            texts = [doc["content"] for doc in batch]
            metadatas = [
                {
                    "domain": doc.get("domain", "unknown"),
                    "source": doc.get("source", "unknown"),
                    "title": doc.get("title", "unknown"),
                }
                for doc in batch
            ]
            try:
                self.collection.upsert(
                    ids=ids,
                    documents=texts,
                    metadatas=metadatas,
                )
                total_indexed += len(batch)
            except Exception as e:
                logger.error(f"Failed to index batch {i // batch_size}: {e}")

        self._is_indexed = total_indexed > 0
        logger.info(f"Indexed {total_indexed} documents into vector store")
        return total_indexed

    def query(
        self,
        query_text: str,
        n_results: int = 5,
        domain_filter: str | None = None,
    ) -> list[dict[str, Any]]:
        if not self.is_indexed:
            logger.warning("Vector store not indexed, returning empty results")
            return []

        where = {"domain": domain_filter} if domain_filter else None
        try:
            results = self.collection.query(
                query_texts=[query_text],
                n_results=n_results,
                where=where,
                include=["documents", "metadatas", "distances"],
            )
        except Exception as e:
            logger.error(f"Query failed: {e}")
            return []

        documents = []
        if results and results.get("documents"):
            for i, doc in enumerate(results["documents"][0]):
                metadata = results["metadatas"][0][i] if results.get("metadatas") else {}
                distance = results["distances"][0][i] if results.get("distances") else 0.0
                score = 1.0 - distance  # Convert cosine distance to similarity
                documents.append({
                    "id": results["ids"][0][i] if results.get("ids") else f"result_{i}",
                    "content": doc,
                    "domain": metadata.get("domain", "unknown"),
                    "source": metadata.get("source", "unknown"),
                    "title": metadata.get("title", "unknown"),
                    "score": max(0.0, score),
                })
        return documents
