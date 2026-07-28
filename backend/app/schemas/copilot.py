from pydantic import BaseModel, Field
from typing import Optional
from uuid import uuid4


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
