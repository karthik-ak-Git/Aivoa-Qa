"""One-time script: Upload all knowledge-base documents to Supabase."""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import httpx
import json
from pathlib import Path
from app.core.config import get_settings
from app.knowledge.loader import load_knowledge_base, find_knowledge_base

settings = get_settings()
SUPABASE_URL = settings.SUPABASE_URL
SERVICE_KEY = settings.SUPABASE_SERVICE_ROLE_KEY
REST_URL = f"{SUPABASE_URL}/rest/v1"
HEADERS = {
    "apikey": SERVICE_KEY,
    "Authorization": f"Bearer {SERVICE_KEY}",
    "Content-Type": "application/json",
    "Prefer": "return=representation",
}


def upload_documents(docs: list[dict]) -> int:
    """Upload documents in batches of 50."""
    batch_size = 50
    total = 0
    for i in range(0, len(docs), batch_size):
        batch = docs[i:i + batch_size]
        rows = []
        for doc in batch:
            rows.append({
                "title": doc["title"][:500],
                "content": doc["content"],
                "domain": doc["domain"],
                "source": doc["source"],
                "chunk_index": doc["metadata"]["chunk_index"],
                "total_chunks": doc["metadata"]["total_chunks"],
                "chunk_size": len(doc["content"]),
                "is_active": True,
            })
        try:
            resp = httpx.post(
                f"{REST_URL}/knowledge_documents",
                json=rows,
                headers=HEADERS,
                timeout=30,
            )
            if resp.status_code in (200, 201):
                total += len(batch)
                print(f"  Uploaded batch {i//batch_size + 1}: {len(batch)} docs (total: {total})")
            else:
                print(f"  Batch {i//batch_size + 1} failed: {resp.status_code} {resp.text[:200]}")
        except Exception as e:
            print(f"  Batch {i//batch_size + 1} error: {e}")
    return total


def upload_source_summary(docs: list[dict]) -> int:
    """Upload source summaries to knowledge_sources table."""
    sources = {}
    for doc in docs:
        src = doc["source"]
        if src not in sources:
            sources[src] = {"source": src, "doc_count": 0, "domains": set()}
        sources[src]["doc_count"] += 1
        sources[src]["domains"].add(doc["domain"])

    count = 0
    for src, info in sources.items():
        row = {
            "source": info["source"],
            "doc_count": info["doc_count"],
            "domains": json.dumps(list(info["domains"])),
        }
        try:
            resp = httpx.post(
                f"{REST_URL}/knowledge_sources",
                json=row,
                headers=HEADERS,
                timeout=10,
            )
            if resp.status_code in (200, 201):
                count += 1
        except Exception:
            pass
    return count


def main():
    print("=== PharmaQMS Knowledge Upload to Supabase ===\n")

    # Check connection
    print("1. Testing Supabase connection...")
    try:
        resp = httpx.get(
            f"{REST_URL}/knowledge_documents?select=id&limit=1",
            headers=HEADERS,
            timeout=10,
        )
        if resp.status_code == 200:
            existing = len(resp.json())
            print(f"   Connected. Existing docs in Supabase: {existing}")
        elif resp.status_code == 404:
            print("   knowledge_documents table not found!")
            print("   Please run schema.sql in Supabase Dashboard > SQL Editor first.")
            return
        else:
            print(f"   Connection issue: {resp.status_code}")
            return
    except Exception as e:
        print(f"   Connection failed: {e}")
        return

    # Load knowledge base
    print("\n2. Loading knowledge base from files...")
    docs = load_knowledge_base()
    print(f"   Loaded {len(docs)} document chunks from {find_knowledge_base()}")

    # Upload documents
    print(f"\n3. Uploading {len(docs)} documents to Supabase...")
    uploaded = upload_documents(docs)
    print(f"   Uploaded: {uploaded}/{len(docs)}")

    # Upload source summaries
    print("\n4. Uploading source summaries...")
    sources_uploaded = upload_source_summary(docs)
    print(f"   Sources uploaded: {sources_uploaded}")

    # Verify
    print("\n5. Verifying...")
    resp = httpx.get(
        f"{REST_URL}/knowledge_documents?select=id",
        headers=HEADERS,
        timeout=10,
    )
    if resp.status_code == 200:
        total_in_db = len(resp.json())
        print(f"   Total docs now in Supabase: {total_in_db}")
    else:
        print(f"   Verification failed: {resp.status_code}")

    print("\n=== Done! ===")


if __name__ == "__main__":
    main()
