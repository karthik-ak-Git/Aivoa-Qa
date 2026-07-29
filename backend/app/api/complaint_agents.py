"""API endpoints for the 3 specialized complaint agents."""
import json
from fastapi import APIRouter, UploadFile, File, Form, HTTPException
from pydantic import BaseModel, Field
from app.graph.complaint_workflow import ComplaintWorkflow
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
    """Extract complaint data from an uploaded document or pasted text."""
    workflow = _get_workflow()

    content = text
    filename = file.filename if file else "unknown"

    if file and not text:
        raw = await file.read()
        try:
            content = raw.decode("utf-8")
        except UnicodeDecodeError:
            try:
                content = raw.decode("latin-1")
            except Exception:
                raise HTTPException(status_code=400, detail="Cannot read file as text. Please paste the document content instead.")

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


@router.post("/chat")
async def legacy_chat(req: WriteRequest):
    """Backward-compatible chat endpoint — routes to writer agent."""
    return await write_complaint(req)
