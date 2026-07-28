import enum
from sqlalchemy import String, Text, Enum, ForeignKey, Integer, DateTime, JSON
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.models.base import Base, TimestampMixin, generate_uuid


class ComplaintStatus(str, enum.Enum):
    OPEN = "open"
    UNDER_REVIEW = "under_review"
    INVESTIGATION = "investigation"
    CAPA_REQUIRED = "capa_required"
    RESOLVED = "resolved"
    CLOSED = "closed"
    REJECTED = "rejected"


class ComplaintPriority(str, enum.Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"


class ComplaintSource(str, enum.Enum):
    PHONE = "phone"
    EMAIL = "email"
    WEB = "web"
    REGULATORY = "regulatory"
    INTERNAL = "internal"
    DISTRIBUTOR = "distributor"
    PATIENT = "patient"


class Complaint(Base, TimestampMixin):
    """Core complaint model with full tracking."""
    __tablename__ = "complaints"

    id: Mapped[str] = mapped_column(
        String(36), primary_key=True, default=generate_uuid
    )
    complaint_number: Mapped[str] = mapped_column(
        String(50), unique=True, nullable=False, index=True
    )
    title: Mapped[str] = mapped_column(String(500), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False)

    # Classification
    status: Mapped[ComplaintStatus] = mapped_column(
        Enum(ComplaintStatus), default=ComplaintStatus.OPEN, nullable=False
    )
    priority: Mapped[ComplaintPriority] = mapped_column(
        Enum(ComplaintPriority), default=ComplaintPriority.MEDIUM, nullable=False
    )
    source: Mapped[ComplaintSource] = mapped_column(
        Enum(ComplaintSource), default=ComplaintSource.WEB, nullable=False
    )
    category: Mapped[str | None] = mapped_column(String(100), nullable=True, index=True)
    subcategory: Mapped[str | None] = mapped_column(String(100), nullable=True)

    # Product info
    product_name: Mapped[str | None] = mapped_column(String(255), nullable=True, index=True)
    product_code: Mapped[str | None] = mapped_column(String(50), nullable=True)
    batch_number: Mapped[str | None] = mapped_column(String(50), nullable=True)
    manufacture_date: Mapped[str | None] = mapped_column(String(20), nullable=True)
    expiry_date: Mapped[str | None] = mapped_column(String(20), nullable=True)

    # Reporter info
    reporter_name: Mapped[str | None] = mapped_column(String(255), nullable=True)
    reporter_email: Mapped[str | None] = mapped_column(String(255), nullable=True)
    reporter_phone: Mapped[str | None] = mapped_column(String(50), nullable=True)
    reporter_type: Mapped[str | None] = mapped_column(String(50), nullable=True)

    # AI Copilot fields
    ai_category: Mapped[str | None] = mapped_column(String(100), nullable=True)
    ai_confidence: Mapped[float | None] = mapped_column(nullable=True)
    ai_suggested_root_cause: Mapped[str | None] = mapped_column(Text, nullable=True)
    ai_suggested_capa: Mapped[str | None] = mapped_column(Text, nullable=True)

    # Resolution
    root_cause: Mapped[str | None] = mapped_column(Text, nullable=True)
    corrective_action: Mapped[str | None] = mapped_column(Text, nullable=True)
    preventive_action: Mapped[str | None] = mapped_column(Text, nullable=True)
    resolution_notes: Mapped[str | None] = mapped_column(Text, nullable=True)
    resolved_at: Mapped[str | None] = mapped_column(DateTime(timezone=True), nullable=True)

    # Attachments and metadata
    attachments: Mapped[dict | None] = mapped_column(JSON, nullable=True)
    tags: Mapped[list | None] = mapped_column(JSON, nullable=True)
    metadata_json: Mapped[dict | None] = mapped_column("metadata", JSON, nullable=True)

    # Foreign keys
    assignee_id: Mapped[str | None] = mapped_column(
        String(36), ForeignKey("users.id"), nullable=True
    )

    # Relationships
    assignee = relationship("User", back_populates="complaints", foreign_keys=[assignee_id])
    investigations = relationship("Investigation", back_populates="complaint", cascade="all, delete-orphan")
    capas = relationship("CAPA", back_populates="complaint", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Complaint {self.complaint_number}: {self.title[:50]}>"
