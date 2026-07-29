import json
import time
from datetime import datetime, timezone
from uuid import uuid4
from fastapi import APIRouter, HTTPException, Depends, UploadFile, File
from app.schemas.copilot import (
    WriteComplaintRequest,
    WriteComplaintResponse,
    ComplaintExtracted,
    EditComplaintRequest,
    EditComplaintResponse,
    EditExtracted,
    ChatHistoryResponse,
    ChatHistoryMessage,
    DocumentUploadResponse,
)
from app.core.logger import get_logger, PerformanceLogger

logger = get_logger("api.copilot.sub")

router = APIRouter(prefix="/api/copilot", tags=["AI Copilot"])


def _get_llm():
    from app.main import app_state
    if not app_state.get("llm_service"):
        raise HTTPException(status_code=503, detail="LLM service not initialized")
    return app_state["llm_service"]


def _get_conversation_service():
    from app.main import app_state
    if not app_state.get("conversation_service"):
        raise HTTPException(status_code=503, detail="Conversation service not initialized")
    return app_state["conversation_service"]


# ──────────────────────────────────────────────
#  WRITE COMPLAINT VIA CHAT
# ──────────────────────────────────────────────

EXTRACT_COMPLAINT_PROMPT = """You are a pharmaceutical complaint intake assistant.
Extract structured complaint fields from the user's natural language message.

Return ONLY a JSON object with these fields (use null for unknowns):
{
  "title": "string - brief complaint title",
  "description": "string - full complaint description",
  "product_name": "string or null",
  "product_code": "string or null",
  "batch_number": "string or null",
  "category": "string or null (e.g. product_defect, packaging_defect, contamination, labeling, efficacy, adverse_event)",
  "priority": "low|medium|high|critical",
  "source": "chat",
  "reporter_name": "string or null",
  "reporter_email": "string or null",
  "tags": ["array of relevant tags"]
}

User message:
{message}

Return ONLY the JSON object, no other text."""


@router.post(
    "/write-complaint",
    response_model=WriteComplaintResponse,
    summary="Create a complaint via chat",
    description=(
        "Send a natural language message describing a complaint. "
        "The AI extracts structured fields (product, batch, category, etc.) "
        "and creates the complaint automatically."
    ),
    responses={
        200: {"description": "Complaint created via chat"},
        503: {"description": "LLM service not available"},
    },
)
async def write_complaint_via_chat(
    request: WriteComplaintRequest,
    llm=Depends(_get_llm),
    conv_service=Depends(_get_conversation_service),
):
    start_time = time.time()

    # Create or get conversation
    conversation = conv_service.get_or_create(request.conversation_id)
    conversation_id = conversation.conversation_id
    conv_service.add_user_message(conversation_id, request.message)

    # Ask AI to extract complaint fields
    prompt = EXTRACT_COMPLAINT_PROMPT.format(message=request.message)
    messages = [
        {"role": "system", "content": "You are a pharmaceutical complaint intake assistant. Return ONLY valid JSON."},
        {"role": "user", "content": prompt},
    ]

    with PerformanceLogger("copilot.write_complaint.llm", logger):
        llm_response = await llm.agenerate(messages)

    # Parse extracted fields
    try:
        # Strip markdown code fences if present
        clean = llm_response.strip()
        if clean.startswith("```"):
            clean = clean.split("\n", 1)[1]
        if clean.endswith("```"):
            clean = clean.rsplit("```", 1)[0]
        clean = clean.strip()
        extracted = json.loads(clean)
    except (json.JSONDecodeError, IndexError):
        logger.error(f"Failed to parse LLM extraction: {llm_response[:300]}")
        raise HTTPException(status_code=500, detail="AI failed to extract complaint fields")

    extracted_model = ComplaintExtracted(**extracted)

    # Create complaint via complaints API logic
    complaint_id = str(uuid4())
    now = datetime.now(timezone.utc)
    year = now.year
    complaint_number = f"CMP-{year}-{int(time.time()) % 100000:05d}"

    complaint_record = {
        "id": complaint_id,
        "complaint_number": complaint_number,
        "title": extracted_model.title,
        "description": extracted_model.description,
        "status": "open",
        "priority": extracted_model.priority or "medium",
        "source": "chat",
        "category": extracted_model.category,
        "product_name": extracted_model.product_name,
        "product_code": extracted_model.product_code,
        "batch_number": extracted_model.batch_number,
        "reporter_name": extracted_model.reporter_name,
        "reporter_email": extracted_model.reporter_email,
        "tags": extracted_model.tags,
        "created_at": datetime.now(timezone.utc).isoformat(),
        "updated_at": datetime.now(timezone.utc).isoformat(),
    }

    # Store complaint
    from app.api.complaints import _complaints_store
    _complaints_store[complaint_id] = complaint_record

    # Try Supabase
    try:
        from app.services.supabase_service import get_supabase_service
        sb = get_supabase_service()
        if sb.url:
            await sb.insert("complaints", complaint_record)
    except Exception:
        pass

    # AI confirmation message
    ai_message = (
        f"Complaint **{complaint_number}** has been created successfully.\n\n"
        f"**Title:** {extracted_model.title}\n"
        f"**Product:** {extracted_model.product_name or 'Not specified'}\n"
        f"**Batch:** {extracted_model.batch_number or 'Not specified'}\n"
        f"**Priority:** {extracted_model.priority}\n"
        f"**Category:** {extracted_model.category or 'Not classified'}\n\n"
        f"You can track this complaint using ID `{complaint_number}`."
    )

    conv_service.add_assistant_message(
        conversation_id=conversation_id,
        content=ai_message,
        agent_used="complaint_agent",
        citations=[],
    )

    processing_time_ms = (time.time() - start_time) * 1000
    logger.info(f"Write complaint via chat: {complaint_number} in {processing_time_ms:.1f}ms")

    return WriteComplaintResponse(
        conversation_id=conversation_id,
        ai_message=ai_message,
        complaint=complaint_record,
        extracted_fields=extracted_model,
        confidence=0.85,
    )


# ──────────────────────────────────────────────
#  EDIT COMPLAINT VIA CHAT
# ──────────────────────────────────────────────

EXTRACT_EDIT_PROMPT = """You are a pharmaceutical complaint editing assistant.
The user wants to edit an existing complaint. Extract the fields to update from their message.

Current complaint state:
{complaint_json}

User instruction:
{message}

Return ONLY a JSON object:
{{
  "fields_to_update": {{
    "field_name": "new_value",
    ...
  }},
  "reasoning": "Explanation of what changes were made and why"
}}

Valid field names: title, description, status, priority, category, subcategory,
product_name, product_code, batch_number, root_cause, corrective_action,
preventive_action, resolution_notes, reporter_name, reporter_email, tags

Return ONLY the JSON object, no other text."""


@router.post(
    "/edit-complaint",
    response_model=EditComplaintResponse,
    summary="Edit a complaint via chat",
    description=(
        "Provide a complaint ID and a natural language instruction to edit it. "
        "The AI extracts the changes and applies them."
    ),
    responses={
        200: {"description": "Complaint edited"},
        404: {"description": "Complaint not found"},
        503: {"description": "LLM service not available"},
    },
)
async def edit_complaint_via_chat(
    request: EditComplaintRequest,
    llm=Depends(_get_llm),
    conv_service=Depends(_get_conversation_service),
):
    start_time = time.time()

    # Find complaint
    from app.api.complaints import _complaints_store
    complaint = _complaints_store.get(request.complaint_id)
    if not complaint:
        # Search by complaint_number
        for r in _complaints_store.values():
            if r.get("complaint_number") == request.complaint_id:
                complaint = r
                break

    if not complaint:
        raise HTTPException(status_code=404, detail=f"Complaint '{request.complaint_id}' not found")

    complaint_before = dict(complaint)

    # Conversation
    conversation = conv_service.get_or_create(request.conversation_id)
    conversation_id = conversation.conversation_id
    conv_service.add_user_message(conversation_id, request.message)

    # Ask AI to extract edit operations
    prompt = EXTRACT_EDIT_PROMPT.format(
        complaint_json=json.dumps(complaint, indent=2, default=str),
        message=request.message,
    )
    messages = [
        {"role": "system", "content": "You are a complaint editing assistant. Return ONLY valid JSON."},
        {"role": "user", "content": prompt},
    ]

    with PerformanceLogger("copilot.edit_complaint.llm", logger):
        llm_response = await llm.agenerate(messages)

    # Parse
    try:
        clean = llm_response.strip()
        if clean.startswith("```"):
            clean = clean.split("\n", 1)[1]
        if clean.endswith("```"):
            clean = clean.rsplit("```", 1)[0]
        clean = clean.strip()
        parsed = json.loads(clean)
    except (json.JSONDecodeError, IndexError):
        raise HTTPException(status_code=500, detail="AI failed to extract edit operations")

    fields_to_update = parsed.get("fields_to_update", {})
    reasoning = parsed.get("reasoning", "No reasoning provided")

    if not fields_to_update:
        raise HTTPException(status_code=400, detail="AI could not determine what to change")

    # Whitelist allowed fields - prevent AI from overwriting id, timestamps, etc.
    ALLOWED_EDIT_FIELDS = {
        "title", "description", "status", "priority", "category", "subcategory",
        "product_name", "product_code", "batch_number", "root_cause",
        "corrective_action", "preventive_action", "resolution_notes",
        "reporter_name", "reporter_email", "tags",
    }
    # Validate status/priority enums
    VALID_STATUSES = {"open", "in_progress", "under_review", "closed", "resolved", "rejected"}
    VALID_PRIORITIES = {"low", "medium", "high", "critical"}

    fields_to_update = {k: v for k, v in fields_to_update.items() if k in ALLOWED_EDIT_FIELDS}
    if "status" in fields_to_update and fields_to_update["status"] not in VALID_STATUSES:
        fields_to_update.pop("status")
    if "priority" in fields_to_update and fields_to_update["priority"] not in VALID_PRIORITIES:
        fields_to_update.pop("priority")

    if not fields_to_update:
        raise HTTPException(status_code=400, detail="No valid fields to update")

    # Apply updates
    fields_to_update["updated_at"] = datetime.now(timezone.utc).isoformat()
    complaint.update(fields_to_update)

    # Try Supabase
    try:
        from app.services.supabase_service import get_supabase_service
        sb = get_supabase_service()
        if sb.url:
            await sb.update("complaints", data=fields_to_update, filters={"id": complaint["id"]})
    except Exception:
        pass

    # AI confirmation
    changes_list = "\n".join(f"- **{k}**: `{complaint_before.get(k, 'N/A')}` → `{v}`" for k, v in fields_to_update.items() if k != "updated_at")
    ai_message = (
        f"Complaint **{complaint['complaint_number']}** has been updated.\n\n"
        f"**Changes:**\n{changes_list}\n\n"
        f"**Reasoning:** {reasoning}"
    )

    conv_service.add_assistant_message(
        conversation_id=conversation_id,
        content=ai_message,
        agent_used="complaint_agent",
        citations=[],
    )

    processing_time_ms = (time.time() - start_time) * 1000
    logger.info(f"Edit complaint via chat: {complaint['complaint_number']} in {processing_time_ms:.1f}ms")

    return EditComplaintResponse(
        conversation_id=conversation_id,
        ai_message=ai_message,
        complaint_before=complaint_before,
        complaint_after=dict(complaint),
        edit_details=EditExtracted(fields_to_update=fields_to_update, reasoning=reasoning),
        confidence=0.85,
    )


# ──────────────────────────────────────────────
#  CHAT HISTORY
# ──────────────────────────────────────────────

@router.get(
    "/chat/history/{conversation_id}",
    response_model=ChatHistoryResponse,
    summary="Get chat history",
    description="Retrieve the full message history for a conversation.",
    responses={
        200: {"description": "Chat history returned"},
        404: {"description": "Conversation not found"},
    },
)
async def get_chat_history(
    conversation_id: str,
    conv_service=Depends(_get_conversation_service),
):
    conversation = conv_service.get(conversation_id)
    if not conversation:
        raise HTTPException(status_code=404, detail=f"Conversation '{conversation_id}' not found")

    messages = [
        ChatHistoryMessage(
            role=m.role,
            content=m.content,
            timestamp=m.timestamp.isoformat() if m.timestamp else "",
            agent_used=m.agent_used,
            citations=m.citations or [],
        )
        for m in conversation.messages
    ]

    return ChatHistoryResponse(
        conversation_id=conversation_id,
        messages=messages,
        total_messages=len(messages),
        created_at=conversation.created_at.isoformat() if conversation.created_at else None,
        updated_at=conversation.updated_at.isoformat() if conversation.updated_at else None,
    )


# ──────────────────────────────────────────────
#  LIST CONVERSATIONS
# ──────────────────────────────────────────────

@router.get(
    "/chat/conversations",
    summary="List all conversations",
    description="Returns a list of all active conversation IDs.",
)
async def list_conversations(
    conv_service=Depends(_get_conversation_service),
):
    conversations = conv_service.list_conversations()
    return {"conversations": conversations, "total": len(conversations)}


# ──────────────────────────────────────────────
#  DOCUMENT UPLOAD
# ──────────────────────────────────────────────

EXTRACT_DOC_PROMPT = """You are a pharmaceutical document analyzer.
Analyze the following document content and extract:

1. A summary of the document (2-3 sentences)
2. If this document describes a complaint, extract the complaint fields

Document content (first 3000 chars):
{content}

Return ONLY a JSON object:
{{
  "summary": "2-3 sentence summary",
  "is_complaint": true/false,
  "complaint_fields": {{
    "title": "string or null",
    "description": "string or null",
    "product_name": "string or null",
    "batch_number": "string or null",
    "category": "string or null",
    "priority": "low|medium|high|critical or null",
    "tags": ["array of tags"]
  }}
}}

Return ONLY the JSON object, no other text."""


@router.post(
    "/upload",
    response_model=DocumentUploadResponse,
    summary="Upload a document",
    description=(
        "Upload a document (PDF, DOCX, TXT, MD). "
        "The text is extracted and optionally analyzed by AI "
        "to detect complaint information."
    ),
    responses={
        200: {"description": "Document processed"},
        400: {"description": "Unsupported file type"},
    },
)
async def upload_document(
    file: UploadFile = File(...),
    analyze: bool = True,
    conversation_id: str | None = None,
    llm=Depends(_get_llm),
    conv_service=Depends(_get_conversation_service),
):
    # Validate file type
    ALLOWED_EXTENSIONS = {"txt", "md", "csv", "pdf", "docx"}
    MAX_FILE_SIZE = 10 * 1024 * 1024  # 10 MB

    if not file.filename:
        raise HTTPException(status_code=400, detail="No filename provided")
    ext = file.filename.rsplit(".", 1)[-1].lower() if "." in file.filename else ""
    if ext not in ALLOWED_EXTENSIONS:
        raise HTTPException(status_code=400, detail=f"Unsupported file type: .{ext}")

    # Read file content with size limit
    raw_bytes = await file.read()
    file_size = len(raw_bytes)
    if file_size > MAX_FILE_SIZE:
        raise HTTPException(status_code=413, detail=f"File too large: {file_size} bytes (max {MAX_FILE_SIZE})")
    if file_size == 0:
        raise HTTPException(status_code=400, detail="Empty file")

    # Extract text (in-process, no subprocess)
    text = ""
    if ext in ("txt", "md", "csv"):
        text = raw_bytes.decode("utf-8", errors="replace")
    elif ext == "pdf":
        try:
            import io
            import fitz
            doc = fitz.open(stream=io.BytesIO(raw_bytes), filetype="pdf")
            text = "\n".join(page.get_text() for page in doc)
            doc.close()
        except ImportError:
            try:
                from pdfminer.high_level import extract_text as pdfminer_extract
                import tempfile, os
                with tempfile.NamedTemporaryFile(suffix=".pdf", delete=False) as tmp:
                    tmp.write(raw_bytes)
                    tmp.flush()
                    text = pdfminer_extract(tmp.name)
                    os.unlink(tmp.name)
            except ImportError:
                text = "[PDF text extraction requires PyMuPDF or pdfminer.six]"
        except Exception:
            text = "[PDF content - text extraction failed]"
    elif ext == "docx":
        try:
            import io
            from docx import Document
            doc = Document(io.BytesIO(raw_bytes))
            text = "\n".join(p.text for p in doc.paragraphs)
        except ImportError:
            text = "[DOCX content - python-docx not installed]"
        except Exception:
            text = "[DOCX content - text extraction failed]"
    else:
        text = raw_bytes.decode("utf-8", errors="replace")

    if not text.strip():
        text = "[No text content could be extracted]"

    # AI analysis
    ai_summary = None
    extracted_complaint = None

    if analyze and text and not text.startswith("["):
        try:
            prompt = EXTRACT_DOC_PROMPT.format(content=text[:3000])
            messages = [
                {"role": "system", "content": "You are a document analyzer. Return ONLY valid JSON."},
                {"role": "user", "content": prompt},
            ]
            with PerformanceLogger("copilot.upload.llm", logger):
                llm_response = await llm.agenerate(messages)

            clean = llm_response.strip()
            if clean.startswith("```"):
                clean = clean.split("\n", 1)[1]
            if clean.endswith("```"):
                clean = clean.rsplit("```", 1)[0]
            parsed = json.loads(clean.strip())

            ai_summary = parsed.get("summary")
            if parsed.get("is_complaint") and parsed.get("complaint_fields"):
                extracted_complaint = ComplaintExtracted(**{
                    k: v for k, v in parsed["complaint_fields"].items()
                    if v is not None
                })
        except Exception as e:
            logger.warning(f"Document AI analysis failed: {e}")

    # Add to conversation if provided
    conversation_id_out = conversation_id
    if conversation_id:
        conv_service.add_user_message(conversation_id, f"[Uploaded document: {file.filename}]")
        if ai_summary:
            conv_service.add_assistant_message(
                conversation_id=conversation_id,
                content=f"Document analysis for **{file.filename}**:\n\n{ai_summary}",
                agent_used="summary_agent",
                citations=[],
            )

    logger.info(f"Document uploaded: {file.filename} ({file_size} bytes, {len(text)} chars extracted)")

    return DocumentUploadResponse(
        filename=file.filename or "unknown",
        content_type=file.content_type or "application/octet-stream",
        file_size=file_size,
        text_preview=text[:2000],
        text_length=len(text),
        conversation_id=conversation_id_out,
        ai_summary=ai_summary,
        extracted_complaint_data=extracted_complaint,
    )
