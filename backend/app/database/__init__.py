from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy import text
from app.core.config import get_settings
from app.core.logger import get_logger
from typing import AsyncGenerator
import asyncio

logger = get_logger("database")

engine = None
async_session_factory = None
db_available = False


async def init_db():
    """Initialize database engine. Falls back gracefully if PostgreSQL is unreachable."""
    global engine, async_session_factory, db_available
    settings = get_settings()

    if not settings.DATABASE_URL:
        logger.warning("DATABASE_URL not set — database disabled, using Supabase REST API")
        return

    logger.info("Connecting to Supabase PostgreSQL (5s timeout)...")

    async def _try_connect():
        global engine, async_session_factory, db_available
        engine = create_async_engine(
            settings.DATABASE_URL,
            echo=settings.DEBUG,
            pool_pre_ping=True,
            pool_size=5,
            max_overflow=10,
            connect_args={"timeout": 5, "command_timeout": 5},
        )
        async_session_factory = async_sessionmaker(
            engine, class_=AsyncSession, expire_on_commit=False
        )
        try:
            async with engine.connect() as conn:
                result = await conn.execute(text("SELECT 1"))
                result.fetchone()
            db_available = True
            logger.info("Database connection verified")
        except Exception as e:
            logger.warning(f"Direct PostgreSQL unavailable ({type(e).__name__}) — using Supabase REST API")
            db_available = False

    try:
        await asyncio.wait_for(_try_connect(), timeout=8)
    except asyncio.TimeoutError:
        logger.warning("PostgreSQL connection timed out (8s) — using Supabase REST API")
        db_available = False
        if engine:
            await engine.dispose()
            engine = None
            async_session_factory = None


async def get_db() -> AsyncGenerator[AsyncSession, None]:
    """Dependency that provides a database session (if available)."""
    if not db_available or async_session_factory is None:
        yield None
        return
    async with async_session_factory() as session:
        try:
            yield session
            await session.commit()
        except Exception:
            await session.rollback()
            raise


async def close_db():
    """Dispose of the database engine."""
    global engine, async_session_factory, db_available
    if engine:
        await engine.dispose()
        engine = None
        async_session_factory = None
        db_available = False
    logger.info("Database connections closed")


async def create_tables():
    """Create all tables if direct DB is available."""
    global engine
    if engine is None or not db_available:
        logger.info("No direct DB — tables must be created via Supabase Dashboard")
        return

    from app.models import Base
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    logger.info("Database tables created/verified")


async def check_db_health() -> dict:
    """Check database connectivity."""
    global engine
    if not db_available or engine is None:
        return {"status": "rest_api_only", "error": "Direct PostgreSQL unavailable"}
    try:
        async with engine.connect() as conn:
            result = await conn.execute(text("SELECT version()"))
            row = result.fetchone()
            return {"status": "connected", "version": row[0] if row else "unknown"}
    except Exception as e:
        return {"status": "error", "error": str(e)}
