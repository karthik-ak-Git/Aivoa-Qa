from pydantic_settings import BaseSettings
from pydantic import Field
from typing import Optional
from functools import lru_cache


class Settings(BaseSettings):
    """Application configuration loaded from environment variables."""

    # Application
    APP_NAME: str = "PharmaQMS AI Copilot"
    APP_VERSION: str = "1.0.0"
    DEBUG: bool = Field(default=False)
    HOST: str = "0.0.0.0"
    PORT: int = 8000

    # CORS
    CORS_ORIGINS: list[str] = ["http://localhost:5173", "http://localhost:3000", "http://127.0.0.1:5173"]

    # Supabase
    SUPABASE_URL: str = ""
    SUPABASE_ANON_KEY: str = ""
    SUPABASE_SERVICE_ROLE_KEY: str = ""
    SUPABASE_PROJECT_ID: str = ""

    # Database (Supabase PostgreSQL)
    DATABASE_URL: str = ""

    # Groq API (fallback)
    GROQ_API_KEY: str = ""
    GROQ_MODEL: str = "llama-3.3-70b-versatile"
    GROQ_TEMPERATURE: float = 0.3
    GROQ_MAX_TOKENS: int = 2048

    # OpenRouter API (primary)
    OPENROUTER_API_KEY: str = ""
    OPENROUTER_MODEL: str = "google/gemma-4-26b-a4b-it:free"
    OPENROUTER_TEMPERATURE: float = 0.3
    OPENROUTER_MAX_TOKENS: int = 2048
    OPENROUTER_BASE_URL: str = "https://openrouter.ai/api/v1"

    # Embedding
    EMBEDDING_MODEL: str = "sentence-transformers/all-MiniLM-L6-v2"
    EMBEDDING_DIMENSION: int = 384

    # Vector Store
    VECTOR_DB_PATH: str = "./data/chroma_db"
    VECTOR_COLLECTION_NAME: str = "pharmaqms_knowledge"
    CHUNK_SIZE: int = 512
    CHUNK_OVERLAP: int = 100

    # Redis (optional)
    REDIS_URL: Optional[str] = None
    REDIS_TTL: int = 3600

    # Knowledge Base
    KNOWLEDGE_BASE_PATH: str = "../../knowledge-base"

    # Logging
    LOG_LEVEL: str = "INFO"
    LOG_FORMAT: str = "%(asctime)s | %(levelname)-8s | %(name)s | %(message)s"

    # Timeouts
    LLM_TIMEOUT: int = 60
    RETRIEVAL_TIMEOUT: int = 30

    model_config = {
        "env_file": ".env",
        "env_file_encoding": "utf-8",
        "case_sensitive": True,
    }


@lru_cache
def get_settings() -> Settings:
    return Settings()
