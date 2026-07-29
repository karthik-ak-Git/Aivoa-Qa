import os
import json
from pathlib import Path
from typing import Any
from app.core.logger import get_logger

logger = get_logger("knowledge.loader")


def find_knowledge_base() -> str:
    backend_dir = Path(__file__).parent.parent.parent  # backend/
    project_root = backend_dir.parent  # project root (Aivoa-Qa/)
    candidates = [
        project_root / "knowledge-base",
        backend_dir / "knowledge-base",
        Path("knowledge-base"),
    ]
    for candidate in candidates:
        if candidate.exists():
            return str(candidate.resolve())
    raise FileNotFoundError(
        f"Knowledge base directory not found. Tried: {[str(c) for c in candidates]}"
    )


def load_knowledge_base() -> list[dict[str, Any]]:
    """Load from Supabase. Falls back to local files if Supabase unavailable."""
    try:
        docs = _load_from_supabase()
        if docs:
            return docs
    except Exception as e:
        logger.warning(f"Supabase load failed ({e}), falling back to local files")

    return _load_from_files()


def _load_from_supabase() -> list[dict[str, Any]]:
    """Load all knowledge documents from Supabase."""
    import httpx
    from app.core.config import get_settings

    settings = get_settings()
    if not settings.SUPABASE_URL or not settings.SUPABASE_SERVICE_ROLE_KEY:
        return []

    rest_url = f"{settings.SUPABASE_URL}/rest/v1"
    headers = {
        "apikey": settings.SUPABASE_SERVICE_ROLE_KEY,
        "Authorization": f"Bearer {settings.SUPABASE_SERVICE_ROLE_KEY}",
    }

    docs = []
    offset = 0
    batch_size = 1000

    while True:
        resp = httpx.get(
            f"{rest_url}/knowledge_documents",
            params={
                "select": "id,title,content,domain,source,chunk_index,total_chunks",
                "order": "domain,chunk_index",
                "limit": str(batch_size),
                "offset": str(offset),
            },
            headers=headers,
            timeout=30,
        )
        resp.raise_for_status()
        rows = resp.json()
        if not rows:
            break

        for row in rows:
            docs.append({
                "id": row["id"],
                "content": row["content"],
                "domain": row["domain"],
                "source": row["source"],
                "title": row["title"],
                "metadata": {
                    "domain": row["domain"],
                    "source_file": row["source"],
                    "chunk_index": row["chunk_index"],
                    "total_chunks": row["total_chunks"],
                },
            })

        offset += batch_size
        if len(rows) < batch_size:
            break

    logger.info(f"Loaded {len(docs)} documents from Supabase")
    return docs


def _load_from_files() -> list[dict[str, Any]]:
    """Load from local knowledge-base files (fallback)."""
    from app.knowledge.loader_files import KNOWLEDGE_DOMAINS, chunk_document

    kb_path = find_knowledge_base()
    documents = []
    for domain, info in KNOWLEDGE_DOMAINS.items():
        file_path = os.path.join(kb_path, info["path"])
        if not os.path.exists(file_path):
            logger.warning(f"Knowledge file not found: {file_path}")
            continue
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
            chunks = chunk_document(content, domain)
            for i, chunk in enumerate(chunks):
                documents.append({
                    "id": f"{domain}_{i}",
                    "content": chunk,
                    "domain": domain,
                    "source": info["path"],
                    "title": f"{domain} - chunk {i}",
                    "metadata": {
                        "domain": domain,
                        "description": info["description"],
                        "source_file": info["path"],
                        "chunk_index": i,
                        "total_chunks": len(chunks),
                    },
                })
            logger.info(f"Loaded {len(chunks)} chunks from domain: {domain}")
        except Exception as e:
            logger.error(f"Failed to load domain {domain}: {e}")
    logger.info(f"Total documents loaded: {len(documents)}")
    return documents
