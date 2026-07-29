from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


# ──────────────────────────────────────────────
#  ORIGINAL COPILOT SCHEMAS
# ──────────────────────────────────────────────


class CopilotRequest(BaseModel):
    """Request schema for the AI Copilot chat endpoint."""

    message: str = Field(
        ...,
        min_length=1,
        max_length=5000,
        description="The user's message or question about pharmaceutical complaints",
        json_schema_extra={"example": "What are the root causes of tablet capping defects?"}
    )
    conversation_id: Optional[str] = Field(
        default=None,
        description="Existing conversation ID for continuing a thread",
        json_schema_extra={"example": "conv_abc123"}
    )
    complaint_id: Optional[str] = Field(
        default=None,
        description="Related complaint ID for context-specific assistance",
        json_schema_extra={"example": "CMP-2026-00142"}
    )
    user_id: Optional[str] = Field(
        default=None,
        description="User identifier for personalization and audit trail",
        json_schema_extra={"example": "user_001"}
    )


class Citation(BaseModel):
    """A citation referencing a knowledge base document."""

    source: str = Field(
        ...,
        description="Name or path of the source document",
        json_schema_extra={"example": "root_cause_library.md"}
    )
    domain: str = Field(
        ...,
        description="Knowledge domain the citation belongs to",
        json_schema_extra={"example": "root_cause_library"}
    )
    section: Optional[str] = Field(
        default=None,
        description="Specific section or heading within the source",
        json_schema_extra={"example": "6M Root Cause Categories"}
    )
    confidence: float = Field(
        default=0.0,
        ge=0.0,
        le=1.0,
        description="Confidence score of this citation"
    )
    snippet: Optional[str] = Field(
        default=None,
        description="Relevant text snippet from the source"
    )


class CopilotResponse(BaseModel):
    """Response schema for the AI Copilot chat endpoint."""

    response: str = Field(
        ...,
        description="The AI-generated response to the user's message"
    )
    conversation_id: str = Field(
        ...,
        description="Conversation identifier (new or existing)"
    )
    citations: list[Citation] = Field(
        default_factory=list,
        description="Citations from the knowledge base supporting the response"
    )
    sources: list[str] = Field(
        default_factory=list,
        description="Source document names referenced"
    )
    agent_used: str = Field(
        ...,
        description="Name of the AI agent that generated the response"
    )
    confidence: float = Field(
        ...,
        ge=0.0,
        le=1.0,
        description="Overall confidence score of the response"
    )
    processing_time_ms: Optional[float] = Field(
        default=None,
        description="Total processing time in milliseconds"
    )


# ──────────────────────────────────────────────
#  WRITE COMPLAINT VIA CHAT
# ──────────────────────────────────────────────


class WriteComplaintRequest(BaseModel):
    """Request to create a complaint via natural language chat."""

    message: str = Field(
        ...,
        min_length=5,
        max_length=5000,
        description="Natural language description of the complaint",
        json_schema_extra={
            "example": "We found capping issues on tablets from batch BT-041. About 15% of tablets are affected. Product is Aspirin 325mg."
        },
    )
    conversation_id: Optional[str] = Field(
        default=None,
        description="Conversation ID to continue a thread",
    )
    user_id: Optional[str] = Field(
        default=None,
        description="User ID for audit trail",
    )


class ComplaintExtracted(BaseModel):
    """AI-extracted complaint fields from natural language."""

    title: str = Field(..., description="Extracted complaint title")
    description: str = Field(..., description="Full complaint description")
    product_name: Optional[str] = Field(default=None)
    product_code: Optional[str] = Field(default=None)
    batch_number: Optional[str] = Field(default=None)
    category: Optional[str] = Field(default=None)
    priority: Optional[str] = Field(default="medium")
    source: Optional[str] = Field(default="chat")
    reporter_name: Optional[str] = Field(default=None)
    reporter_email: Optional[str] = Field(default=None)
    tags: Optional[list[str]] = Field(default=None)


class WriteComplaintResponse(BaseModel):
    """Response after creating a complaint via chat."""

    conversation_id: str
    ai_message: str = Field(description="AI confirmation message summarizing what was created")
    complaint: dict = Field(description="Created complaint data")
    extracted_fields: ComplaintExtracted
    confidence: float = Field(ge=0.0, le=1.0)


# ──────────────────────────────────────────────
#  EDIT COMPLAINT VIA CHAT
# ──────────────────────────────────────────────


class EditComplaintRequest(BaseModel):
    """Request to edit a complaint via natural language chat."""

    complaint_id: str = Field(
        ...,
        description="Complaint ID or complaint number to edit",
        json_schema_extra={"example": "CMP-2026-00001"},
    )
    message: str = Field(
        ...,
        min_length=5,
        max_length=5000,
        description="Natural language instruction on what to change",
        json_schema_extra={"example": "Change the priority to high and add root cause: insufficient granulation moisture"},
    )
    conversation_id: Optional[str] = Field(
        default=None,
        description="Conversation ID to continue a thread",
    )
    user_id: Optional[str] = Field(
        default=None,
        description="User ID for audit trail",
    )


class EditExtracted(BaseModel):
    """AI-extracted edit operations."""

    fields_to_update: dict = Field(
        description="Extracted field updates as key-value pairs",
        json_schema_extra={
            "example": {"priority": "high", "root_cause": "Insufficient granulation moisture"}
        },
    )
    reasoning: str = Field(description="Why these changes were made")


class EditComplaintResponse(BaseModel):
    """Response after editing a complaint via chat."""

    conversation_id: str
    ai_message: str = Field(description="AI confirmation message summarizing changes")
    complaint_before: dict = Field(description="Complaint state before edit")
    complaint_after: dict = Field(description="Complaint state after edit")
    edit_details: EditExtracted
    confidence: float = Field(ge=0.0, le=1.0)


# ──────────────────────────────────────────────
#  CHAT HISTORY
# ──────────────────────────────────────────────


class ChatHistoryMessage(BaseModel):
    """Single message in chat history."""

    role: str
    content: str
    timestamp: str
    agent_used: Optional[str] = None
    citations: Optional[list[dict]] = None


class ChatHistoryResponse(BaseModel):
    """Full chat history for a conversation."""

    conversation_id: str
    messages: list[ChatHistoryMessage]
    total_messages: int
    created_at: Optional[str] = None
    updated_at: Optional[str] = None


# ──────────────────────────────────────────────
#  DOCUMENT UPLOAD
# ──────────────────────────────────────────────


class DocumentUploadResponse(BaseModel):
    """Response after uploading a document."""

    filename: str
    content_type: str
    file_size: int
    text_preview: str = Field(description="First 2000 chars of extracted text")
    text_length: int = Field(description="Total extracted text length")
    conversation_id: Optional[str] = None
    ai_summary: Optional[str] = Field(default=None, description="AI-generated summary of the document")
    extracted_complaint_data: Optional[ComplaintExtracted] = Field(
        default=None,
        description="If the document contains complaint info, extracted fields",
    )
