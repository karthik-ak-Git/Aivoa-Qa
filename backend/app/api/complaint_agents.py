"""API endpoints for the complaint agents — write, edit, and OCR extraction."""
import json
from fastapi import APIRouter, UploadFile, File, Form, HTTPException
from pydantic import BaseModel, Field
from app.graph.complaint_workflow import ComplaintWorkflow
from app.services.ocr_service import extract_text_from_bytes
from app.core.logger import get_logger

logger = get_logger("api.complaint_agents")

router = APIRouter(prefix="/api/copilot", tags=["copilot-agents"])

# Workflow instance — set by main.py during startup
_workflow: ComplaintWorkflow | None = None


def set_workflow(workflow: ComplaintWorkflow):
    global _workflow
    _workflow = workflow


def _get_workflow() -> ComplaintWorkflow:
    if _workflow is None:
        raise HTTPException(status_code=503, detail="Complaint workflow not initialized")
    return _workflow


# ── Request / Response schemas ──

class WriteRequest(BaseModel):
    query: str = Field(..., description="Natural language description of the complaint")
    current_form: dict | None = Field(None, description="Existing form data to reference")


class EditRequest(BaseModel):
    instruction: str = Field(..., description="Edit instruction from the user")
    current_form: dict = Field(..., description="Current complaint form data")


class CopilotResponse(BaseModel):
    form_data: dict
    confidence: float
    agent_used: str
    sources_used: list[str]


# ── Endpoints ──

@router.post("/write", response_model=CopilotResponse)
async def write_complaint(req: WriteRequest):
    """Write a new complaint from a natural language description."""
    workflow = _get_workflow()
    result = await workflow.run(mode="write", query=req.query, current_form=req.current_form)
    return CopilotResponse(
        form_data=result["form_data"],
        confidence=result["confidence"],
        agent_used=result["agent_used"],
        sources_used=result.get("sources_used", []),
    )


@router.post("/edit", response_model=CopilotResponse)
async def edit_complaint(req: EditRequest):
    """Edit an existing complaint based on user instruction."""
    workflow = _get_workflow()
    result = await workflow.run(
        mode="edit",
        query=req.instruction,
        current_form=req.current_form,
    )
    return CopilotResponse(
        form_data=result["form_data"],
        confidence=result["confidence"],
        agent_used=result["agent_used"],
        sources_used=result.get("sources_used", []),
    )


@router.post("/extract", response_model=CopilotResponse)
async def extract_from_document(
    file: UploadFile = File(None),
    text: str = Form(default=""),
):
    """Extract complaint data from an uploaded document (PDF, image, DOCX, TXT) or pasted text."""
    workflow = _get_workflow()
    filename = file.filename if file else "pasted_text.txt"

    if file and not text:
        raw = await file.read()
        ext = filename.rsplit(".", 1)[-1].lower() if "." in filename else ""
        if ext in ("png", "jpg", "jpeg", "tiff", "tif", "bmp", "pdf", "docx"):
            result = extract_text_from_bytes(raw, filename)
            content = result["text"]
            logger.info(f"File extraction: method={result['method']}, success={result['success']}, chars={len(content)}")
        else:
            content = raw.decode("utf-8", errors="replace")
    else:
        content = text

    if not content.strip():
        raise HTTPException(status_code=400, detail="No content to extract from.")

    result = await workflow.run(mode="ocr", query=content, filename=filename)
    return CopilotResponse(
        form_data=result["form_data"],
        confidence=result["confidence"],
        agent_used=result["agent_used"],
        sources_used=result.get("sources_used", []),
    )


class ExtractTextRequest(BaseModel):
    text: str = Field(..., description="Document text to extract from")
    filename: str = Field(default="unknown", description="Original filename")


@router.post("/extract-text", response_model=CopilotResponse)
async def extract_from_text(req: ExtractTextRequest):
    """Extract complaint data from pasted text (no file upload needed)."""
    workflow = _get_workflow()
    result = await workflow.run(mode="ocr", query=req.text, filename=req.filename)
    return CopilotResponse(
        form_data=result["form_data"],
        confidence=result["confidence"],
        agent_used=result["agent_used"],
        sources_used=result.get("sources_used", []),
    )


class LegacyChatRequest(BaseModel):
    message: str = Field(..., description="User message (backward compat)")
    query: str | None = Field(None, description="Alternative query field")
    conversation_id: str | None = None
    complaint_id: str | None = None
    user_id: str | None = None


@router.post("/chat", response_model=CopilotResponse)
async def legacy_chat(req: LegacyChatRequest):
    """Backward-compatible chat endpoint — routes to writer agent."""
    query = req.query or req.message
    return await write_complaint(WriteRequest(query=query))
