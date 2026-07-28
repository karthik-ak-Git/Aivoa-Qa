from uuid import uuid4
from app.schemas.conversation import ConversationContext
from app.core.logger import get_logger

logger = get_logger("services.conversation")


class ConversationService:
    """In-memory conversation memory service."""

    def __init__(self):
        self._conversations: dict[str, ConversationContext] = {}

    def get_or_create(self, conversation_id: str | None) -> ConversationContext:
        if conversation_id and conversation_id in self._conversations:
            return self._conversations[conversation_id]
        cid = conversation_id or str(uuid4())
        context = ConversationContext(
            conversation_id=cid,
            messages=[],
        )
        self._conversations[cid] = context
        logger.info(f"Created conversation: {cid}")
        return context

    def get(self, conversation_id: str) -> ConversationContext | None:
        return self._conversations.get(conversation_id)

    def add_user_message(self, conversation_id: str, content: str) -> None:
        ctx = self.get_or_create(conversation_id)
        ctx.add_message("user", content)

    def add_assistant_message(
        self,
        conversation_id: str,
        content: str,
        agent_used: str = "",
        citations: list[dict] | None = None,
    ) -> None:
        ctx = self.get_or_create(conversation_id)
        ctx.add_message(
            "assistant",
            content,
            agent_used=agent_used,
            citations=citations or [],
        )

    def update_retrieved_docs(self, conversation_id: str, docs: list[dict]) -> None:
        ctx = self.get(conversation_id)
        if ctx:
            ctx.last_retrieved_docs = docs

    def update_active_domain(self, conversation_id: str, domain: str) -> None:
        ctx = self.get(conversation_id)
        if ctx:
            ctx.active_domain = domain

    def clear(self, conversation_id: str) -> bool:
        if conversation_id in self._conversations:
            del self._conversations[conversation_id]
            return True
        return False

    def list_conversations(self) -> list[str]:
        return list(self._conversations.keys())
