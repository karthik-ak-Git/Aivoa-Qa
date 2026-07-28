from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class ConversationMessage(BaseModel):
    """A single message in a conversation."""

    role: str = Field(
        ...,
        description="Message role: 'user' or 'assistant'"
    )
    content: str = Field(
        ...,
        description="Message content"
    )
    timestamp: datetime = Field(
        default_factory=datetime.utcnow,
        description="Message timestamp"
    )
    agent_used: Optional[str] = Field(
        default=None,
        description="Agent used to generate the response (if role is assistant)"
    )
    citations: list[dict] = Field(
        default_factory=list,
        description="Citations included in the response"
    )
    metadata: dict = Field(
        default_factory=dict,
        description="Additional metadata about the message"
    )


class ConversationContext(BaseModel):
    """Full conversation context maintained for a session."""

    conversation_id: str = Field(
        ...,
        description="Unique conversation identifier"
    )
    messages: list[ConversationMessage] = Field(
        default_factory=list,
        description="Ordered list of messages in the conversation"
    )
    complaint_id: Optional[str] = Field(
        default=None,
        description="Related complaint ID"
    )
    user_id: Optional[str] = Field(
        default=None,
        description="User identifier"
    )
    active_domain: Optional[str] = Field(
        default=None,
        description="Currently active knowledge domain"
    )
    last_retrieved_docs: list[dict] = Field(
        default_factory=list,
        description="Most recently retrieved documents"
    )
    created_at: datetime = Field(
        default_factory=datetime.utcnow,
        description="Conversation creation timestamp"
    )
    updated_at: datetime = Field(
        default_factory=datetime.utcnow,
        description="Last update timestamp"
    )

    def add_message(self, role: str, content: str, **kwargs) -> None:
        self.messages.append(
            ConversationMessage(role=role, content=content, **kwargs)
        )
        self.updated_at = datetime.utcnow()

    def get_history(self, limit: int = 20) -> list[dict]:
        recent = self.messages[-limit:]
        return [{"role": m.role, "content": m.content} for m in recent]
