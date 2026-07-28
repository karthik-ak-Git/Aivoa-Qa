from typing import Any
from app.retriever.vector_store import VectorStore
from app.knowledge.loader import KNOWLEDGE_DOMAINS
from app.core.logger import get_logger

logger = get_logger("retriever.service")


class RetrievalService:
    """Reusable retrieval layer for knowledge documents."""

    def __init__(self, vector_store: VectorStore):
        self.vector_store = vector_store

    def retrieve_documents(
        self,
        query: str,
        n_results: int = 5,
        domain_filter: str | None = None,
    ) -> list[dict[str, Any]]:
        results = self.vector_store.query(
            query_text=query,
            n_results=n_results,
            domain_filter=domain_filter,
        )
        logger.info(
            f"Retrieved {len(results)} documents for query: '{query[:80]}...' "
            f"(domain={domain_filter}, score_range="
            f"{min(r['score'] for r in results) if results else 0:.3f}-"
            f"{max(r['score'] for r in results) if results else 0:.3f})"
        )
        return results

    def retrieve_by_category(
        self,
        category: str,
        query: str = "",
        n_results: int = 5,
    ) -> list[dict[str, Any]]:
        if category not in KNOWLEDGE_DOMAINS:
            logger.warning(f"Unknown category: {category}")
            return self.vector_store.query(query_text=query or category, n_results=n_results)

        effective_query = query if query else KNOWLEDGE_DOMAINS[category]["description"]
        return self.vector_store.query(
            query_text=effective_query,
            n_results=n_results,
            domain_filter=category,
        )

    def retrieve_by_similarity(
        self,
        query: str,
        n_results: int = 10,
        min_score: float = 0.3,
    ) -> list[dict[str, Any]]:
        results = self.vector_store.query(query_text=query, n_results=n_results)
        filtered = [r for r in results if r["score"] >= min_score]
        logger.info(f"Similarity retrieval: {len(filtered)}/{len(results)} above threshold {min_score}")
        return filtered

    def retrieve_for_agent(
        self,
        query: str,
        agent_domains: list[str],
        n_results: int = 5,
    ) -> list[dict[str, Any]]:
        all_results = []
        per_domain = max(2, n_results // len(agent_domains)) if agent_domains else n_results

        for domain in agent_domains:
            domain_results = self.vector_store.query(
                query_text=query,
                n_results=per_domain,
                domain_filter=domain,
            )
            all_results.extend(domain_results)

        all_results.sort(key=lambda x: x.get("score", 0), reverse=True)
        return all_results[:n_results]

    def get_stats(self) -> dict[str, Any]:
        return {
            "total_documents": self.vector_store.collection.count(),
            "is_indexed": self.vector_store.is_indexed,
            "available_domains": list(KNOWLEDGE_DOMAINS.keys()),
        }
