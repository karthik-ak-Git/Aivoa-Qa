import uuid
from datetime import datetime, timezone
from fastapi import APIRouter, HTTPException, Query
from typing import Optional
from app.schemas.complaint import (
    CreateComplaint,
    ComplaintResponse,
    ComplaintListResponse,
    ComplaintUpdate,
)
from app.core.logger import get_logger

logger = get_logger("api.complaints")
router = APIRouter(prefix="/api/complaints", tags=["Complaints"])

# In-memory store (used when Supabase is unavailable)
_complaints_store: dict[str, dict] = {}
_complaint_counter: int = 0


def _generate_complaint_number() -> str:
    global _complaint_counter
    _complaint_counter += 1
    year = datetime.now(timezone.utc).year
    return f"CMP-{year}-{_complaint_counter:05d}"


def _now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


async def _get_supabase():
    """Try to get Supabase service, return None if unavailable."""
    try:
        from app.services.supabase_service import get_supabase_service
        sb = get_supabase_service()
        if sb.url:
            return sb
    except Exception:
        pass
    return None


def _to_response(data: dict) -> ComplaintResponse:
    """Convert raw dict to ComplaintResponse, handling missing fields."""
    return ComplaintResponse(
        id=data.get("id", ""),
        complaint_number=data.get("complaint_number", ""),
        title=data.get("title", ""),
        description=data.get("description", ""),
        status=data.get("status", "open"),
        priority=data.get("priority", "medium"),
        source=data.get("source", "web"),
        category=data.get("category"),
        subcategory=data.get("subcategory"),
        product_name=data.get("product_name"),
        product_code=data.get("product_code"),
        batch_number=data.get("batch_number"),
        manufacture_date=data.get("manufacture_date"),
        expiry_date=data.get("expiry_date"),
        reporter_name=data.get("reporter_name"),
        reporter_email=data.get("reporter_email"),
        reporter_type=data.get("reporter_type"),
        ai_category=data.get("ai_category"),
        ai_confidence=data.get("ai_confidence"),
        ai_suggested_root_cause=data.get("ai_suggested_root_cause"),
        ai_suggested_capa=data.get("ai_suggested_capa"),
        root_cause=data.get("root_cause"),
        corrective_action=data.get("corrective_action"),
        preventive_action=data.get("preventive_action"),
        resolution_notes=data.get("resolution_notes"),
        tags=data.get("tags"),
        assignee_id=data.get("assignee_id"),
        created_at=data.get("created_at", _now_iso()),
        updated_at=data.get("updated_at", _now_iso()),
    )


# ── POST /api/complaints ──

@router.post(
    "",
    response_model=ComplaintResponse,
    status_code=201,
    summary="Create a new complaint",
    description="Submit a new pharmaceutical quality complaint for tracking and investigation.",
    responses={
        201: {"description": "Complaint created successfully"},
        422: {"description": "Validation error in request body"},
    },
)
async def create_complaint(request: CreateComplaint):
    complaint_id = str(uuid.uuid4())
    complaint_number = _generate_complaint_number()
    now = _now_iso()

    record = {
        "id": complaint_id,
        "complaint_number": complaint_number,
        "title": request.title,
        "description": request.description,
        "status": "open",
        "priority": request.priority or "medium",
        "source": request.source or "web",
        "category": request.category,
        "subcategory": None,
        "product_name": request.product_name,
        "product_code": request.product_code,
        "batch_number": request.batch_number,
        "manufacture_date": None,
        "expiry_date": None,
        "reporter_name": request.reporter_name,
        "reporter_email": request.reporter_email,
        "reporter_phone": request.reporter_phone,
        "reporter_type": request.reporter_type,
        "ai_category": None,
        "ai_confidence": None,
        "ai_suggested_root_cause": None,
        "ai_suggested_capa": None,
        "root_cause": None,
        "corrective_action": None,
        "preventive_action": None,
        "resolution_notes": None,
        "tags": request.tags,
        "assignee_id": None,
        "created_at": now,
        "updated_at": now,
    }

    # Try Supabase first
    sb = await _get_supabase()
    if sb:
        try:
            result = await sb.insert("complaints", record)
            if result:
                # Supabase REST returns a list; use first item if present
                if isinstance(result, list) and len(result) > 0:
                    record = result[0]
                elif isinstance(result, dict):
                    record = result
            logger.info(f"Complaint created in Supabase: {complaint_number}")
        except Exception as e:
            logger.warning(f"Supabase insert failed, using in-memory store: {e}")
            _complaints_store[complaint_id] = record
    else:
        _complaints_store[complaint_id] = record

    logger.info(f"Complaint created: {complaint_number} - {request.title[:50]}")
    return _to_response(record)


# ── GET /api/complaints ──

@router.get(
    "",
    response_model=ComplaintListResponse,
    summary="List complaints",
    description="Retrieve a paginated list of complaints with optional filters.",
)
async def list_complaints(
    page: int = Query(1, ge=1, description="Page number"),
    page_size: int = Query(20, ge=1, le=100, description="Items per page"),
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    category: Optional[str] = Query(None, description="Filter by category"),
    search: Optional[str] = Query(None, description="Search in title and description"),
):
    sb = await _get_supabase()

    if sb:
        try:
            filters = {}
            if status:
                filters["status"] = status
            if priority:
                filters["priority"] = priority
            if category:
                filters["category"] = category

            all_records = await sb.select(
                "complaints",
                columns="*",
                filters=filters if filters else None,
                order="created_at.desc",
                limit=1000,
            )

            # Apply search filter in-memory (PostgREST doesn't support LIKE easily)
            if search and all_records:
                search_lower = search.lower()
                all_records = [
                    r for r in all_records
                    if search_lower in (r.get("title", "") or "").lower()
                    or search_lower in (r.get("description", "") or "").lower()
                ]

            total = len(all_records) if all_records else 0
            start = (page - 1) * page_size
            end = start + page_size
            paged = all_records[start:end] if all_records else []

            return ComplaintListResponse(
                complaints=[_to_response(r) for r in paged],
                total=total,
                page=page,
                page_size=page_size,
            )
        except Exception as e:
            logger.warning(f"Supabase query failed, using in-memory store: {e}")

    # Fallback: in-memory
    records = list(_complaints_store.values())

    if status:
        records = [r for r in records if r.get("status") == status]
    if priority:
        records = [r for r in records if r.get("priority") == priority]
    if category:
        records = [r for r in records if r.get("category") == category]
    if search:
        search_lower = search.lower()
        records = [
            r for r in records
            if search_lower in (r.get("title", "") or "").lower()
            or search_lower in (r.get("description", "") or "").lower()
        ]

    records.sort(key=lambda r: r.get("created_at", ""), reverse=True)
    total = len(records)
    start = (page - 1) * page_size
    paged = records[start : start + page_size]

    return ComplaintListResponse(
        complaints=[_to_response(r) for r in paged],
        total=total,
        page=page,
        page_size=page_size,
    )


# ── GET /api/complaints/{complaint_id} ──

@router.get(
    "/{complaint_id}",
    response_model=ComplaintResponse,
    summary="Get complaint details",
    description="Retrieve full details of a specific complaint by its ID or complaint number.",
    responses={
        200: {"description": "Complaint found"},
        404: {"description": "Complaint not found"},
    },
)
async def get_complaint(complaint_id: str):
    sb = await _get_supabase()

    if sb:
        try:
            # Try by ID first
            result = await sb.select_one("complaints", filters={"id": complaint_id})
            if not result:
                # Try by complaint_number
                result = await sb.select_one(
                    "complaints", filters={"complaint_number": complaint_id}
                )
            if result:
                return _to_response(result)
        except Exception as e:
            logger.warning(f"Supabase query failed: {e}")

    # Fallback: in-memory
    record = _complaints_store.get(complaint_id)
    if not record:
        # Search by complaint_number
        for r in _complaints_store.values():
            if r.get("complaint_number") == complaint_id:
                record = r
                break

    if not record:
        raise HTTPException(status_code=404, detail=f"Complaint '{complaint_id}' not found")

    return _to_response(record)


# ── PATCH /api/complaints/{complaint_id} ──

@router.patch(
    "/{complaint_id}",
    response_model=ComplaintResponse,
    summary="Update a complaint",
    description="Update fields on an existing complaint (status, priority, resolution, etc.).",
    responses={
        200: {"description": "Complaint updated"},
        404: {"description": "Complaint not found"},
    },
)
async def update_complaint(complaint_id: str, request: ComplaintUpdate):
    sb = await _get_supabase()

    # Build update payload (only non-None fields)
    update_data = request.model_dump(exclude_unset=True)
    if not update_data:
        raise HTTPException(status_code=400, detail="No fields to update")

    # Validate enums
    VALID_STATUSES = {"open", "in_progress", "under_review", "closed", "resolved", "rejected"}
    VALID_PRIORITIES = {"low", "medium", "high", "critical"}
    if "status" in update_data and update_data["status"] not in VALID_STATUSES:
        raise HTTPException(status_code=400, detail=f"Invalid status. Must be one of: {VALID_STATUSES}")
    if "priority" in update_data and update_data["priority"] not in VALID_PRIORITIES:
        raise HTTPException(status_code=400, detail=f"Invalid priority. Must be one of: {VALID_PRIORITIES}")

    update_data["updated_at"] = _now_iso()

    if sb:
        try:
            # Find by ID or complaint_number
            existing = await sb.select_one("complaints", filters={"id": complaint_id})
            if not existing:
                existing = await sb.select_one(
                    "complaints", filters={"complaint_number": complaint_id}
                )
            if existing:
                await sb.update("complaints", data=update_data, filters={"id": existing["id"]})
                updated = await sb.select_one("complaints", filters={"id": existing["id"]})
                if updated:
                    return _to_response(updated)
        except Exception as e:
            logger.warning(f"Supabase update failed: {e}")

    # Fallback: in-memory
    record = _complaints_store.get(complaint_id)
    if not record:
        for r in _complaints_store.values():
            if r.get("complaint_number") == complaint_id:
                record = r
                break

    if not record:
        raise HTTPException(status_code=404, detail=f"Complaint '{complaint_id}' not found")

    record.update(update_data)
    return _to_response(record)


# ── DELETE /api/complaints/{complaint_id} ──

@router.delete(
    "/{complaint_id}",
    status_code=204,
    summary="Delete a complaint",
    description="Permanently delete a complaint by its ID or complaint number.",
    responses={
        204: {"description": "Complaint deleted"},
        404: {"description": "Complaint not found"},
    },
)
async def delete_complaint(complaint_id: str):
    sb = await _get_supabase()

    if sb:
        try:
            existing = await sb.select_one("complaints", filters={"id": complaint_id})
            if not existing:
                existing = await sb.select_one(
                    "complaints", filters={"complaint_number": complaint_id}
                )
            if existing:
                await sb.delete("complaints", filters={"id": existing["id"]})
                logger.info(f"Complaint deleted from Supabase: {complaint_id}")
                return
        except Exception as e:
            logger.warning(f"Supabase delete failed: {e}")

    # Fallback: in-memory
    record = _complaints_store.pop(complaint_id, None)
    if not record:
        for r in list(_complaints_store.values()):
            if r.get("complaint_number") == complaint_id:
                _complaints_store.pop(r["id"], None)
                record = r
                break

    if not record:
        raise HTTPException(status_code=404, detail=f"Complaint '{complaint_id}' not found")

    logger.info(f"Complaint deleted: {complaint_id}")
