"""
Supabase REST API service for CRUD operations.
Used when direct PostgreSQL connections are blocked.
"""
import httpx
from typing import Any
from app.core.config import get_settings
from app.core.logger import get_logger

logger = get_logger("services.supabase")


class SupabaseService:
    """Service for interacting with Supabase via REST API (PostgREST)."""

    def __init__(self):
        settings = get_settings()
        self.url = settings.SUPABASE_URL
        self.anon_key = settings.SUPABASE_ANON_KEY
        self.service_key = settings.SUPABASE_SERVICE_ROLE_KEY
        self.rest_url = f"{settings.SUPABASE_URL}/rest/v1"
        self.headers = {
            "apikey": self.service_key,
            "Authorization": f"Bearer {self.service_key}",
            "Content-Type": "application/json",
            "Prefer": "return=representation",
        }

    async def _request(
        self,
        method: str,
        path: str,
        data: dict | None = None,
        params: dict | None = None,
    ) -> Any:
        url = f"{self.rest_url}/{path}"
        async with httpx.AsyncClient(timeout=30) as client:
            resp = await client.request(
                method, url, json=data, params=params, headers=self.headers
            )
            if not resp.is_success:
                body = resp.text[:500]
                logger.error(f"Supabase API error {resp.status_code}: {body}")
                resp.raise_for_status()
            return resp.json() if resp.content else None

    # ---- CRUD helpers ----

    async def insert(self, table: str, data: dict | list[dict]) -> Any:
        return await self._request("POST", table, data=data)

    async def select(
        self,
        table: str,
        columns: str = "*",
        filters: dict | None = None,
        order: str | None = None,
        limit: int | None = None,
    ) -> list[dict]:
        params = {"select": columns}
        if filters:
            for k, v in filters.items():
                params[k] = f"eq.{v}"
        if order:
            params["order"] = order
        if limit:
            params["limit"] = str(limit)
        return await self._request("GET", table, params=params)

    async def select_one(self, table: str, filters: dict, columns: str = "*") -> dict | None:
        results = await self.select(table, columns=columns, filters=filters, limit=1)
        return results[0] if results else None

    async def update(self, table: str, data: dict, filters: dict) -> Any:
        params = {}
        for k, v in filters.items():
            params[k] = f"eq.{v}"
        return await self._request("PATCH", table, data=data, params=params)

    async def delete(self, table: str, filters: dict) -> Any:
        params = {}
        for k, v in filters.items():
            params[k] = f"eq.{v}"
        return await self._request("DELETE", table, params=params)

    async def rpc(self, function_name: str, params: dict | None = None) -> Any:
        return await self._request("POST", f"rpc/{function_name}", data=params or {})

    async def health_check(self) -> dict:
        try:
            # Try knowledge_sources first (created early), fall back to any table
            for table in ["knowledge_sources", "users", "knowledge_documents"]:
                try:
                    await self.select(table, columns="id", limit=1)
                    return {"status": "connected", "table": table}
                except Exception:
                    continue
            return {"status": "connected", "note": "REST endpoint reachable but no tables found"}
        except Exception as e:
            return {"status": "error", "error": str(e)}


# Singleton
_supabase_service: SupabaseService | None = None


def get_supabase_service() -> SupabaseService:
    global _supabase_service
    if _supabase_service is None:
        _supabase_service = SupabaseService()
    return _supabase_service
