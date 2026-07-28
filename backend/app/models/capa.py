import enum
from sqlalchemy import String, Text, ForeignKey, Enum, DateTime, JSON, Float
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.models.base import Base, TimestampMixin, generate_uuid


class CAPAType(str, enum.Enum):
    CORRECTIVE = "corrective"
    PREVENTIVE = "preventive"
    BOTH = "both"


class CAPAStatus(str, enum.Enum):
    OPEN = "open"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    EFFECTIVENESS_CHECK = "effectiveness_check"
    CLOSED = "closed"
    OVERDUE = "overdue"


class CAPA(Base, TimestampMixin):
    """Corrective and Preventive Action tracking."""
    __tablename__ = "capas"

    id: Mapped[str] = mapped_column(
        String(36), primary_key=True, default=generate_uuid
    )
    capa_number: Mapped[str] = mapped_column(
        String(50), unique=True, nullable=False, index=True
    )
    title: Mapped[str] = mapped_column(String(500), nullable=False)
    description: Mapped[str | None] = mapped_column(Text, nullable=True)

    # CAPA classification
    capa_type: Mapped[CAPAType] = mapped_column(
        Enum(CAPAType), default=CAPAType.CORRECTIVE, nullable=False
    )
    status: Mapped[CAPAStatus] = mapped_column(
        Enum(CAPAStatus), default=CAPAStatus.OPEN, nullable=False
    )

    # Action details
    corrective_action: Mapped[str | None] = mapped_column(Text, nullable=True)
    preventive_action: Mapped[str | None] = mapped_column(Text, nullable=True)
    action_owner: Mapped[str | None] = mapped_column(String(255), nullable=True)
    target_date: Mapped[str | None] = mapped_column(DateTime(timezone=True), nullable=True)
    completed_date: Mapped[str | None] = mapped_column(DateTime(timezone=True), nullable=True)

    # Effectiveness
    effectiveness_criteria: Mapped[str | None] = mapped_column(Text, nullable=True)
    effectiveness_result: Mapped[str | None] = mapped_column(Text, nullable=True)
    effectiveness_date: Mapped[str | None] = mapped_column(DateTime(timezone=True), nullable=True)
    is_effective: Mapped[bool | None] = mapped_column(nullable=True)

    # AI fields
    ai_suggested_actions: Mapped[list | None] = mapped_column(JSON, nullable=True)
    ai_confidence: Mapped[float | None] = mapped_column(nullable=True)

    # Supporting data
    evidence: Mapped[list | None] = mapped_column(JSON, nullable=True)
    attachments: Mapped[dict | None] = mapped_column(JSON, nullable=True)

    # Foreign keys
    complaint_id: Mapped[str] = mapped_column(
        String(36), ForeignKey("complaints.id"), nullable=False
    )
    investigation_id: Mapped[str | None] = mapped_column(
        String(36), ForeignKey("investigations.id"), nullable=True
    )
    created_by_id: Mapped[str | None] = mapped_column(
        String(36), ForeignKey("users.id"), nullable=True
    )

    # Relationships
    complaint = relationship("Complaint", back_populates="capas")

    def __repr__(self):
        return f"<CAPA {self.capa_number}: {self.title[:50]}>"
