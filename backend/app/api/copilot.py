import time
from fastapi import APIRouter, HTTPException, Depends
from app.schemas.copilot import CopilotRequest, CopilotResponse, Citation
from app.core.logger import get_logger, PerformanceLogger
from app.services.conversation_service import ConversationService

logger = get_logger("api.copilot")
router = APIRouter(prefix="/api/copilot", tags=["AI Copilot"])


def get_workflow():
    from app.main import app_state
    if not app_state.get("workflow"):
        raise HTTPException(status_code=503, detail="AI Copilot not initialized")
    return app_state["workflow"]


def get_conversation_service() -> ConversationService:
    from app.main import app_state
    if not app_state.get("conversation_service"):
        raise HTTPException(status_code=503, detail="Conversation service not initialized")
    return app_state["conversation_service"]


@router.post(
    "/chat",
    response_model=CopilotResponse,
    summary="Chat with the AI Copilot",
    description=(
        "Send a message to the Pharmaceutical AI Copilot. "
        "The copilot analyzes the message, retrieves relevant knowledge, "
        "selects the appropriate agent, and generates a grounded response with citations."
    ),
    responses={
        200: {
            "description": "Successful response from the AI Copilot",
            "content": {
                "application/json": {
                    "example": {
                        "response": "Based on the knowledge base, tablet capping is typically caused by...",
                        "conversation_id": "conv_abc123",
                        "citations": [
                            {
                                "source": "root_cause_library.md",
                                "domain": "root_cause_library",
                                "section": "6M Root Cause Categories",
                                "confidence": 0.85,
                                "snippet": "Capping is a tablet defect where..."
                            }
                        ],
                        "sources": ["root_cause_library.md"],
                        "agent_used": "root_cause_agent",
                        "confidence": 0.82,
                        "processing_time_ms": 1250.5,
                    }
                }
            },
        },
        422: {"description": "Validation error in request body"},
        503: {"description": "AI Copilot not initialized"},
    },
)
async def chat(
    request: CopilotRequest,
    workflow=Depends(get_workflow),
    conv_service: ConversationService = Depends(get_conversation_service),
):
    start_time = time.time()

    conversation = conv_service.get_or_create(request.conversation_id)
    conversation_id = conversation.conversation_id

    conv_service.add_user_message(conversation_id, request.message)
    history = conversation.get_history(limit=10)

    initial_state = {
        "message": request.message,
        "conversation_id": conversation_id,
        "complaint_id": request.complaint_id,
        "user_id": request.user_id,
        "conversation_history": history,
        "intent": "",
        "retrieved_docs": [],
        "agent_response": {},
        "citations": [],
        "sources": [],
        "agent_used": "",
        "confidence": 0.0,
        "response": "",
        "validation_result": {},
        "errors": [],
    }

    with PerformanceLogger("copilot.chat.workflow", logger):
        result = await workflow.run(initial_state)

    processing_time_ms = (time.time() - start_time) * 1000

    citations = [
        Citation(
            source=c.get("source", "unknown"),
            domain=c.get("domain", "unknown"),
            section=c.get("section", ""),
            confidence=c.get("confidence", 0.0),
            snippet=c.get("snippet", ""),
        )
        for c in result.get("citations", [])
    ]

    conv_service.add_assistant_message(
        conversation_id=conversation_id,
        content=result["response"],
        agent_used=result.get("agent_used", "unknown"),
        citations=[c.model_dump() for c in citations],
    )

    conv_service.update_retrieved_docs(
        conversation_id, result.get("retrieved_docs", [])
    )

    response = CopilotResponse(
        response=result["response"],
        conversation_id=conversation_id,
        citations=citations,
        sources=result.get("sources", []),
        agent_used=result.get("agent_used", "unknown"),
        confidence=result.get("confidence", 0.0),
        processing_time_ms=round(processing_time_ms, 2),
    )

    logger.info(
        f"Copilot response: agent={response.agent_used}, "
        f"confidence={response.confidence:.3f}, "
        f"citations={len(response.citations)}, "
        f"time={response.processing_time_ms:.1f}ms"
    )

    return response
