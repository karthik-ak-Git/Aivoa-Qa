import uuid
from sqlalchemy import String, Text, ForeignKey, JSON, Integer, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.models.base import Base, TimestampMixin, generate_uuid


class Conversation(Base, TimestampMixin):
    """Chat conversation sessions."""
    __tablename__ = "conversations"

    id: Mapped[str] = mapped_column(
        String(36), primary_key=True, default=generate_uuid
    )
    conversation_id: Mapped[str] = mapped_column(
        String(50), unique=True, nullable=False, index=True,
        default=lambda: f"conv_{uuid.uuid4().hex[:12]}"
    )
    title: Mapped[str | None] = mapped_column(String(500), nullable=True)
    status: Mapped[str] = mapped_column(String(50), default="active", nullable=False)

    # Context
    complaint_id: Mapped[str | None] = mapped_column(
        String(36), ForeignKey("complaints.id"), nullable=True
    )
    agent_used: Mapped[str | None] = mapped_column(String(100), nullable=True)
    metadata_json: Mapped[dict | None] = mapped_column("metadata", JSON, nullable=True)

    # Foreign keys
    user_id: Mapped[str | None] = mapped_column(
        String(36), ForeignKey("users.id"), nullable=True
    )

    # Relationships
    user = relationship("User", back_populates="chat_conversations")
    messages = relationship("ChatMessage", back_populates="conversation", cascade="all, delete-orphan")

    def get_history(self, limit: int = 20) -> list[dict]:
        msgs = sorted(self.messages, key=lambda m: m.created_at)
        recent = msgs[-limit:] if len(msgs) > limit else msgs
        return [{"role": m.role, "content": m.content} for m in recent]

    def __repr__(self):
        return f"<Conversation {self.conversation_id}>"


class ChatMessage(Base, TimestampMixin):
    """Individual messages within a conversation."""
    __tablename__ = "chat_messages"

    id: Mapped[str] = mapped_column(
        String(36), primary_key=True, default=generate_uuid
    )
    role: Mapped[str] = mapped_column(String(20), nullable=False)  # user, assistant, system
    content: Mapped[str] = mapped_column(Text, nullable=False)

    # Agent context
    agent_used: Mapped[str | None] = mapped_column(String(100), nullable=True)
    citations: Mapped[list | None] = mapped_column(JSON, nullable=True)
    confidence: Mapped[float | None] = mapped_column(nullable=True)
    intent: Mapped[str | None] = mapped_column(String(100), nullable=True)

    # Metadata
    tokens_used: Mapped[int | None] = mapped_column(Integer, nullable=True)
    processing_time_ms: Mapped[float | None] = mapped_column(nullable=True)
    metadata_json: Mapped[dict | None] = mapped_column("metadata", JSON, nullable=True)

    # Foreign keys
    conversation_id: Mapped[str] = mapped_column(
        String(36), ForeignKey("conversations.id"), nullable=False
    )

    # Relationships
    conversation = relationship("Conversation", back_populates="messages")

    def __repr__(self):
        return f"<ChatMessage {self.role}: {self.content[:50]}>"
