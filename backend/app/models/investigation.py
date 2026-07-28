from sqlalchemy import String, Text, ForeignKey, JSON, Float
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.models.base import Base, TimestampMixin, generate_uuid


class Investigation(Base, TimestampMixin):
    """Investigation tracking for complaints."""
    __tablename__ = "investigations"

    id: Mapped[str] = mapped_column(
        String(36), primary_key=True, default=generate_uuid
    )
    investigation_number: Mapped[str] = mapped_column(
        String(50), unique=True, nullable=False, index=True
    )
    title: Mapped[str] = mapped_column(String(500), nullable=False)
    description: Mapped[str | None] = mapped_column(Text, nullable=True)

    # Investigation details
    root_cause_category: Mapped[str | None] = mapped_column(String(100), nullable=True)
    root_cause_description: Mapped[str | None] = mapped_column(Text, nullable=True)
    methodology: Mapped[str | None] = mapped_column(String(100), nullable=True)
    evidence: Mapped[list | None] = mapped_column(JSON, nullable=True)
    findings: Mapped[str | None] = mapped_column(Text, nullable=True)

    # 6M Analysis
    man_method: Mapped[str | None] = mapped_column(Text, nullable=True)
    machine_method: Mapped[str | None] = mapped_column(Text, nullable=True)
    material_method: Mapped[str | None] = mapped_column(Text, nullable=True)
    measurement_method: Mapped[str | None] = mapped_column(Text, nullable=True)
    mother_nature_method: Mapped[str | None] = mapped_column(Text, nullable=True)
    management_method: Mapped[str | None] = mapped_column(Text, nullable=True)

    # AI fields
    ai_root_cause_suggestion: Mapped[str | None] = mapped_column(Text, nullable=True)
    ai_confidence: Mapped[float | None] = mapped_column(nullable=True)

    # Status
    status: Mapped[str] = mapped_column(String(50), default="open", nullable=False)
    completed_at: Mapped[str | None] = mapped_column(nullable=True)

    # Foreign keys
    complaint_id: Mapped[str] = mapped_column(
        String(36), ForeignKey("complaints.id"), nullable=False
    )
    investigator_id: Mapped[str | None] = mapped_column(
        String(36), ForeignKey("users.id"), nullable=True
    )

    # Relationships
    complaint = relationship("Complaint", back_populates="investigations")

    def __repr__(self):
        return f"<Investigation {self.investigation_number}>"
