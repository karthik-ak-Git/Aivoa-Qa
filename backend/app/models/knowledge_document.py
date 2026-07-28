from sqlalchemy import String, Text, Integer, JSON, Float, Boolean
from sqlalchemy.orm import Mapped, mapped_column
from app.models.base import Base, TimestampMixin, generate_uuid


class KnowledgeDocument(Base, TimestampMixin):
    """Knowledge base documents for AI retrieval."""
    __tablename__ = "knowledge_documents"

    id: Mapped[str] = mapped_column(
        String(36), primary_key=True, default=generate_uuid
    )
    title: Mapped[str] = mapped_column(String(500), nullable=False)
    content: Mapped[str] = mapped_column(Text, nullable=False)
    domain: Mapped[str] = mapped_column(String(100), nullable=False, index=True)
    source: Mapped[str] = mapped_column(String(500), nullable=False)
    source_url: Mapped[str | None] = mapped_column(Text, nullable=True)

    # Chunking info
    chunk_index: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    total_chunks: Mapped[int] = mapped_column(Integer, default=1, nullable=False)
    chunk_size: Mapped[int] = mapped_column(Integer, default=512, nullable=False)

    # Metadata
    tags: Mapped[list | None] = mapped_column(JSON, nullable=True)
    metadata_json: Mapped[dict | None] = mapped_column("metadata", JSON, nullable=True)
    language: Mapped[str] = mapped_column(String(10), default="en", nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)

    # Embedding reference (stored in ChromaDB, tracked here for sync)
    embedding_id: Mapped[str | None] = mapped_column(String(100), nullable=True, index=True)

    def __repr__(self):
        return f"<KnowledgeDocument {self.domain}: {self.title[:50]}>"
