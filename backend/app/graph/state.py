from typing import TypedDict, Annotated, Any
from operator import add


class CopilotState(TypedDict):
    """State for the LangGraph copilot workflow."""
    message: str
    conversation_id: str
    complaint_id: str | None
    user_id: str | None
    conversation_history: list[dict[str, str]]
    intent: str
    retrieved_docs: list[dict[str, Any]]
    agent_response: dict[str, Any]
    citations: list[dict[str, Any]]
    sources: list[str]
    agent_used: str
    confidence: float
    response: str
    validation_result: dict[str, Any]
    errors: Annotated[list[str], add]
