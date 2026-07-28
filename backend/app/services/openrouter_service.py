"""OpenRouter LLM service — OpenAI-compatible API, free models."""
import httpx
import time
from typing import Any
from app.core.config import get_settings
from app.core.logger import get_logger

logger = get_logger("services.openrouter")


class OpenRouterService:
    """Service for interacting with OpenRouter API (OpenAI-compatible)."""

    def __init__(self):
        settings = get_settings()
        self.api_key = settings.OPENROUTER_API_KEY
        self.model = settings.OPENROUTER_MODEL
        self.temperature = settings.OPENROUTER_TEMPERATURE
        self.max_tokens = settings.OPENROUTER_MAX_TOKENS
        self.base_url = settings.OPENROUTER_BASE_URL

    def _headers(self) -> dict:
        return {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
            "HTTP-Referer": "https://pharmaqms.local",
            "X-Title": "PharmaQMS AI Copilot",
        }

    def generate(
        self,
        messages: list[dict[str, str]],
        temperature: float | None = None,
        max_tokens: int | None = None,
    ) -> str:
        """Synchronous generation via OpenRouter."""
        start = time.time()
        payload = {
            "model": self.model,
            "messages": messages,
            "temperature": temperature or self.temperature,
            "max_tokens": max_tokens or self.max_tokens,
            "top_p": 0.9,
            "stream": False,
        }
        try:
            resp = httpx.post(
                f"{self.base_url}/chat/completions",
                json=payload,
                headers=self._headers(),
                timeout=60,
            )
            resp.raise_for_status()
            data = resp.json()
            content = data["choices"][0]["message"]["content"]
            elapsed = time.time() - start
            usage = data.get("usage", {})
            logger.info(
                f"OpenRouter response in {elapsed:.3f}s "
                f"(tokens={usage.get('total_tokens', 'N/A')})"
            )
            return content
        except httpx.HTTPStatusError as e:
            logger.error(f"OpenRouter HTTP error {e.response.status_code}: {e.response.text[:300]}")
            raise
        except Exception as e:
            logger.error(f"OpenRouter generation failed: {e}")
            raise

    async def agenerate(
        self,
        messages: list[dict[str, str]],
        temperature: float | None = None,
        max_tokens: int | None = None,
    ) -> str:
        """Async generation via OpenRouter."""
        start = time.time()
        payload = {
            "model": self.model,
            "messages": messages,
            "temperature": temperature or self.temperature,
            "max_tokens": max_tokens or self.max_tokens,
            "top_p": 0.9,
            "stream": False,
        }
        try:
            async with httpx.AsyncClient(timeout=60) as client:
                resp = await client.post(
                    f"{self.base_url}/chat/completions",
                    json=payload,
                    headers=self._headers(),
                )
                resp.raise_for_status()
                data = resp.json()
                content = data["choices"][0]["message"]["content"]
                elapsed = time.time() - start
                usage = data.get("usage", {})
                logger.info(
                    f"OpenRouter async response in {elapsed:.3f}s "
                    f"(tokens={usage.get('total_tokens', 'N/A')})"
                )
                return content
        except httpx.HTTPStatusError as e:
            logger.error(f"OpenRouter HTTP error {e.response.status_code}: {e.response.text[:300]}")
            raise
        except Exception as e:
            logger.error(f"OpenRouter async generation failed: {e}")
            raise


# Singleton
_openrouter_service: OpenRouterService | None = None


def get_openrouter_service() -> OpenRouterService:
    global _openrouter_service
    if _openrouter_service is None:
        _openrouter_service = OpenRouterService()
    return _openrouter_service
