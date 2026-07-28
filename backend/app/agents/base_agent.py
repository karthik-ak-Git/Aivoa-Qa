from abc import ABC, abstractmethod
from typing import Any, Protocol
from app.retriever.retrieval_service import RetrievalService
from app.core.logger import get_logger

logger = get_logger("agents.base")


class LLMProtocol(Protocol):
    async def agenerate(self, messages: list[dict[str, str]], temperature: float | None = None, max_tokens: int | None = None) -> str: ...


class BaseAgent(ABC):
    """Base class for all AI agents."""

    def __init__(
        self,
        name: str,
        llm_service: Any,
        retrieval_service: RetrievalService,
        system_prompt: str,
        knowledge_domains: list[str],
    ):
        self.name = name
        self.llm = llm_service
        self.retrieval = retrieval_service
        self.system_prompt = system_prompt
        self.knowledge_domains = knowledge_domains

    def _build_messages(
        self,
        query: str,
        context_docs: list[dict],
        conversation_history: list[dict] | None = None,
    ) -> list[dict[str, str]]:
        context_text = self._format_context(context_docs)
        messages = [{"role": "system", "content": self.system_prompt}]

        if conversation_history:
            messages.extend(conversation_history[-6:])

        user_prompt = (
            f"Knowledge Context:\n{context_text}\n\n"
            f"User Question: {query}\n\n"
            "Answer based on the knowledge context above. "
            "Cite specific sources when possible. "
            "If the context does not contain the answer, state that clearly."
        )
        messages.append({"role": "user", "content": user_prompt})
        return messages

    def _format_context(self, docs: list[dict]) -> str:
        if not docs:
            return "No relevant knowledge found."
        parts = []
        for i, doc in enumerate(docs, 1):
            source = doc.get("source", "unknown")
            domain = doc.get("domain", "unknown")
            score = doc.get("score", 0.0)
            content = doc.get("content", "")[:800]
            parts.append(
                f"[{i}] Source: {source} | Domain: {domain} | Score: {score:.3f}\n{content}"
            )
        return "\n\n".join(parts)

    def _extract_citations(self, docs: list[dict]) -> list[dict]:
        seen = set()
        citations = []
        for doc in docs:
            source = doc.get("source", "unknown")
            if source not in seen:
                seen.add(source)
                citations.append({
                    "source": source,
                    "domain": doc.get("domain", "unknown"),
                    "section": doc.get("title", ""),
                    "confidence": doc.get("score", 0.0),
                    "snippet": doc.get("content", "")[:200],
                })
        return citations

    async def run(
        self,
        query: str,
        conversation_history: list[dict] | None = None,
    ) -> dict[str, Any]:
        docs = self.retrieval.retrieve_for_agent(
            query=query,
            agent_domains=self.knowledge_domains,
            n_results=5,
        )
        messages = self._build_messages(query, docs, conversation_history)
        response_text = await self.llm.agenerate(messages)
        citations = self._extract_citations(docs)
        sources = list(set(d.get("source", "unknown") for d in docs))
        confidence = (
            sum(d.get("score", 0) for d in docs) / len(docs)
            if docs
            else 0.0
        )
        return {
            "response": response_text,
            "citations": citations,
            "sources": sources,
            "agent_used": self.name,
            "confidence": round(min(1.0, confidence), 3),
        }
