from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class CreateComplaint(BaseModel):
    """Request schema for creating a new complaint."""

    title: str = Field(
        ...,
        min_length=3,
        max_length=500,
        description="Brief title of the complaint",
        json_schema_extra={"example": "Tablet capping defect in batch BT-2026-041"}
    )
    description: str = Field(
        ...,
        min_length=10,
        max_length=10000,
        description="Detailed description of the complaint",
        json_schema_extra={"example": "Multiple tablets from batch BT-2026-041 exhibited capping after compression. Approximately 15% of tablets affected."}
    )
    product_name: Optional[str] = Field(
        default=None,
        max_length=255,
        description="Name of the product",
        json_schema_extra={"example": "Aspirin 325mg Tablets"}
    )
    product_code: Optional[str] = Field(
        default=None,
        max_length=50,
        description="Product code or SKU",
        json_schema_extra={"example": "ASP-325-TAB"}
    )
    batch_number: Optional[str] = Field(
        default=None,
        max_length=50,
        description="Batch or lot number",
        json_schema_extra={"example": "BT-2026-041"}
    )
    source: Optional[str] = Field(
        default="web",
        description="Complaint source: phone, email, web, regulatory, internal, distributor, patient",
    )
    priority: Optional[str] = Field(
        default="medium",
        description="Priority level: low, medium, high, critical",
    )
    reporter_name: Optional[str] = Field(
        default=None,
        max_length=255,
        description="Name of the person reporting the complaint",
    )
    reporter_email: Optional[str] = Field(
        default=None,
        max_length=255,
        description="Email of the reporter",
    )
    reporter_phone: Optional[str] = Field(
        default=None,
        max_length=50,
        description="Phone of the reporter",
    )
    reporter_type: Optional[str] = Field(
        default=None,
        max_length=50,
        description="Type of reporter: patient, healthcare_professional, distributor, internal, regulatory",
    )
    category: Optional[str] = Field(
        default=None,
        max_length=100,
        description="Complaint category",
        json_schema_extra={"example": "product_defect"}
    )
    tags: Optional[list[str]] = Field(
        default=None,
        description="Tags for filtering",
        json_schema_extra={"example": ["capping", "tablet_defect", "batch_issue"]}
    )


class ComplaintResponse(BaseModel):
    """Response schema for a single complaint."""

    id: str = Field(..., description="Unique complaint ID")
    complaint_number: str = Field(..., description="Human-readable complaint number")
    title: str
    description: str
    status: str = Field(..., description="Current status: open, under_review, investigation, capa_required, resolved, closed, rejected")
    priority: str
    source: str
    category: Optional[str] = None
    subcategory: Optional[str] = None

    product_name: Optional[str] = None
    product_code: Optional[str] = None
    batch_number: Optional[str] = None
    manufacture_date: Optional[str] = None
    expiry_date: Optional[str] = None

    reporter_name: Optional[str] = None
    reporter_email: Optional[str] = None
    reporter_type: Optional[str] = None

    ai_category: Optional[str] = None
    ai_confidence: Optional[float] = None
    ai_suggested_root_cause: Optional[str] = None
    ai_suggested_capa: Optional[str] = None

    root_cause: Optional[str] = None
    corrective_action: Optional[str] = None
    preventive_action: Optional[str] = None
    resolution_notes: Optional[str] = None

    tags: Optional[list[str]] = None

    assignee_id: Optional[str] = None
    created_at: datetime
    updated_at: datetime


class ComplaintListResponse(BaseModel):
    """Paginated list of complaints."""

    complaints: list[ComplaintResponse]
    total: int
    page: int
    page_size: int


class ComplaintUpdate(BaseModel):
    """Request schema for updating a complaint."""

    title: Optional[str] = Field(default=None, min_length=3, max_length=500)
    description: Optional[str] = Field(default=None, min_length=10, max_length=10000)
    status: Optional[str] = Field(default=None, description="New status")
    priority: Optional[str] = Field(default=None, description="New priority")
    category: Optional[str] = None
    subcategory: Optional[str] = None
    root_cause: Optional[str] = None
    corrective_action: Optional[str] = None
    preventive_action: Optional[str] = None
    resolution_notes: Optional[str] = None
    assignee_id: Optional[str] = None
    tags: Optional[list[str]] = None
