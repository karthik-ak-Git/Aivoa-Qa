from fastapi import APIRouter
from datetime import datetime
from app.core.config import get_settings

router = APIRouter(tags=["Health"])


@router.get(
    "/health",
    summary="Health check",
    description="Returns the health status of the API and its dependencies.",
)
async def health_check():
    from app.main import app_state
    from app.database import check_db_health

    settings = get_settings()

    components = {
        "api": "operational",
        "vector_store": "operational" if app_state.get("retrieval_service") else "initializing",
        "llm_service": "operational" if app_state.get("llm_service") else "initializing",
        "knowledge_base": "indexed" if app_state.get("is_indexed") else "not_indexed",
    }

    # Check database
    db_health = await check_db_health()
    components["database"] = db_health["status"]
    if db_health.get("version"):
        components["database_version"] = db_health["version"]

    # Check Supabase REST API
    if app_state.get("supabase_service"):
        try:
            from app.services.supabase_service import get_supabase_service
            sb = get_supabase_service()
            # Quick health check via REST
            import httpx
            async with httpx.AsyncClient(timeout=10) as client:
                resp = await client.get(
                    f"{sb.rest_url}/users?select=id&limit=1",
                    headers={"apikey": sb.service_key, "Authorization": f"Bearer {sb.service_key}"}
                )
                components["supabase_rest"] = "operational" if resp.status_code < 400 else "error"
        except Exception:
            components["supabase_rest"] = "error"

    status = "healthy"
    if any(v in ("initializing", "error", "disconnected") for v in components.values()):
        status = "degraded"

    return {
        "status": status,
        "version": settings.APP_VERSION,
        "timestamp": datetime.utcnow().isoformat(),
        "components": components,
    }


@router.get(
    "/stats",
    summary="System statistics",
    description="Returns statistics about the knowledge base and system state.",
)
async def get_stats():
    from app.main import app_state

    stats = {}
    if app_state.get("retrieval_service"):
        stats = app_state["retrieval_service"].get_stats()
    if app_state.get("conversation_service"):
        stats["active_conversations"] = len(
            app_state["conversation_service"].list_conversations()
        )
    stats["database"] = "connected" if app_state.get("db_initialized") else "disconnected"
    stats["tables_created"] = app_state.get("db_tables_created", False)
    return stats
