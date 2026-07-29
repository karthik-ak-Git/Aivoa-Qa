import time
from contextlib import asynccontextmanager
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from app.core.config import get_settings
from app.core.logger import setup_logging, get_logger
from app.api.complaint_agents import router as agents_router
from app.api.health import router as health_router
from app.api.complaints import router as complaints_router

settings = get_settings()
logger = setup_logging()
get_logger("main")

app_state: dict = {}


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info(f"Starting {settings.APP_NAME} v{settings.APP_VERSION}")
    start = time.time()

    try:
        # Initialize database (graceful fallback if PostgreSQL unreachable)
        from app.database import init_db, create_tables, close_db
        await init_db()
        app_state["db_initialized"] = True
        from app.database import db_available
        app_state["db_available"] = db_available
        if db_available:
            try:
                await create_tables()
                app_state["db_tables_created"] = True
            except Exception as e:
                logger.warning(f"Table creation skipped: {e}")
                app_state["db_tables_created"] = False
        else:
            logger.info("Using Supabase REST API for database operations")
            app_state["db_tables_created"] = False

        # Initialize Supabase REST API service
        from app.services.supabase_service import get_supabase_service
        supabase_service = get_supabase_service()
        app_state["supabase_service"] = supabase_service
        logger.info("Supabase REST API service initialized")

        from app.knowledge.loader import load_knowledge_base
        from app.retriever.vector_store import VectorStore
        from app.retriever.retrieval_service import RetrievalService
        from app.services.groq_service import get_groq_service
        from app.graph.complaint_workflow import ComplaintWorkflow
        from app.services.openrouter_service import get_openrouter_service
        from app.services.conversation_service import ConversationService
        from app.services.validation_service import ResponseValidationService

        # Load knowledge base
        logger.info("Loading knowledge base...")
        documents = load_knowledge_base()
        app_state["knowledge_documents"] = documents

        # Initialize vector store (skip if already indexed)
        logger.info("Initializing vector store...")
        vector_store = VectorStore()
        indexed = vector_store.index_documents(documents)
        app_state["vector_store"] = vector_store
        app_state["is_indexed"] = indexed > 0

        # Store knowledge doc metadata in Supabase
        if indexed > 0:
            try:
                unique_sources = list({d.get("source", "unknown") for d in documents})
                for src in unique_sources:
                    await supabase_service.rpc("upsert_knowledge_source", {
                        "p_source": src,
                        "p_doc_count": len([d for d in documents if d.get("source") == src]),
                    })
                logger.info(f"Synced {len(unique_sources)} knowledge sources to Supabase")
            except Exception as e:
                logger.warning(f"Supabase knowledge sync skipped (table may not exist): {e}")

        # Initialize services
        retrieval_service = RetrievalService(vector_store)
        llm_service = get_openrouter_service()
        conversation_service = ConversationService()
        validation_service = ResponseValidationService()

        app_state["retrieval_service"] = retrieval_service
        app_state["llm_service"] = llm_service
        app_state["conversation_service"] = conversation_service
        app_state["validation_service"] = validation_service

        # Initialize new complaint agents (Writer, Editor, OCR)
        logger.info("Initializing Complaint Agents (Writer + Editor + OCR)...")
        groq_service = get_groq_service()
        complaint_workflow = ComplaintWorkflow(groq=groq_service, retrieval=retrieval_service)
        app_state["complaint_workflow"] = complaint_workflow
        from app.api.complaint_agents import set_workflow
        set_workflow(complaint_workflow)
        logger.info("Complaint agents ready: Writer (gemma2-9b-it), Editor (gemma2-9b-it), OCR (gemma2-9b-it)")

        elapsed = time.time() - start
        logger.info(f"{settings.APP_NAME} ready in {elapsed:.2f}s ({indexed} docs indexed)")

    except Exception as e:
        logger.error(f"Startup failed: {e}")
        app_state["startup_error"] = str(e)

    yield

    logger.info("Shutting down...")
    from app.database import close_db
    try:
        await close_db()
    except Exception:
        pass
    app_state.clear()


app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description=(
        "AI Copilot for Pharmaceutical Customer Complaint Management. "
        "Provides intelligent assistance for complaint classification, "
        "root cause analysis, CAPA generation, and regulatory compliance."
    ),
    docs_url="/docs",
    redoc_url="/redoc",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(agents_router)
app.include_router(health_router)
app.include_router(complaints_router)


@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    logger.error(f"Unhandled exception: {exc}", exc_info=True)
    return JSONResponse(
        status_code=500,
        content={
            "detail": "Internal server error",
            "error": "An unexpected error occurred" if not settings.DEBUG else str(exc)[:200],
        },
    )


@app.exception_handler(404)
async def not_found_handler(request: Request, exc):
    return JSONResponse(
        status_code=404,
        content={"detail": "Resource not found"},
    )