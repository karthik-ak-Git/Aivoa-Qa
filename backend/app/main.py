import time
from contextlib import asynccontextmanager
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from app.core.config import get_settings
from app.core.logger import setup_logging, get_logger
from app.api.copilot import router as copilot_router
from app.api.copilot_sub import router as copilot_sub_router
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
        from app.services.openrouter_service import get_openrouter_service
        from app.services.conversation_service import ConversationService
        from app.services.validation_service import ResponseValidationService
        from app.agents.medicine_agent import MedicineAgent
        from app.agents.complaint_agent import ComplaintAgent
        from app.agents.root_cause_agent import RootCauseAgent
        from app.agents.capa_agent import CAPAAgent
        from app.agents.regulatory_agent import RegulatoryAgent
        from app.agents.summary_agent import SummaryAgent
        from app.graph.workflow import CopilotWorkflow

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

        # Initialize agents
        logger.info("Initializing AI agents...")
        medicine_agent = MedicineAgent(llm_service, retrieval_service)
        complaint_agent = ComplaintAgent(llm_service, retrieval_service)
        root_cause_agent = RootCauseAgent(llm_service, retrieval_service)
        capa_agent = CAPAAgent(llm_service, retrieval_service)
        regulatory_agent = RegulatoryAgent(llm_service, retrieval_service)
        summary_agent = SummaryAgent(llm_service, retrieval_service)

        app_state["agents"] = {
            "medicine": medicine_agent,
            "complaint": complaint_agent,
            "root_cause": root_cause_agent,
            "capa": capa_agent,
            "regulatory": regulatory_agent,
            "summary": summary_agent,
        }

        # Initialize LangGraph workflow
        logger.info("Building LangGraph workflow...")
        workflow = CopilotWorkflow(
            medicine_agent=medicine_agent,
            complaint_agent=complaint_agent,
            root_cause_agent=root_cause_agent,
            capa_agent=capa_agent,
            regulatory_agent=regulatory_agent,
            summary_agent=summary_agent,
            validation_service=validation_service,
            retrieval_service=retrieval_service,
        )
        app_state["workflow"] = workflow

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

app.include_router(copilot_router)
app.include_router(copilot_sub_router)
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
