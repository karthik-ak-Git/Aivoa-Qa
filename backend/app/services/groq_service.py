"""Groq LLM service — gemma2-9b-it primary, llama-3.3-70b-versatile fallback."""
import httpx
import time
from app.core.config import get_settings
from app.core.logger import get_logger

logger = get_logger("services.groq")


class GroqService:
    """Groq API client for fast LLM inference."""

    def __init__(self):
        settings = get_settings()
        self.api_key = settings.GROQ_API_KEY
        self.model = settings.GROQ_MODEL or "llama-3.3-70b-versatile"
        self.fallback_model = "llama-3.1-8b-instant"
        self.temperature = settings.GROQ_TEMPERATURE
        self.max_tokens = settings.GROQ_MAX_TOKENS
        self.base_url = "https://api.groq.com/openai/v1"

    def _headers(self) -> dict:
        return {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }

    def generate(
        self,
        messages: list[dict[str, str]],
        temperature: float | None = None,
        max_tokens: int | None = None,
        model: str | None = None,
    ) -> str:
        start = time.time()
        payload = {
            "model": model or self.model,
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
                f"Groq ({payload['model']}) response in {elapsed:.3f}s "
                f"(tokens={usage.get('total_tokens', 'N/A')})"
            )
            return content
        except httpx.HTTPStatusError as e:
            logger.error(f"Groq HTTP error {e.response.status_code}: {e.response.text[:300]}")
            # Fallback to secondary model
            if payload["model"] == self.model:
                logger.info(f"Falling back to {self.fallback_model}")
                return self.generate(messages, temperature, max_tokens, self.fallback_model)
            raise
        except Exception as e:
            logger.error(f"Groq generation failed: {e}")
            raise

    async def agenerate(
        self,
        messages: list[dict[str, str]],
        temperature: float | None = None,
        max_tokens: int | None = None,
        model: str | None = None,
    ) -> str:
        start = time.time()
        payload = {
            "model": model or self.model,
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
                    f"Groq async ({payload['model']}) response in {elapsed:.3f}s "
                    f"(tokens={usage.get('total_tokens', 'N/A')})"
                )
                return content
        except httpx.HTTPStatusError as e:
            logger.error(f"Groq async HTTP error {e.response.status_code}: {e.response.text[:300]}")
            if payload["model"] == self.model:
                logger.info(f"Falling back to {self.fallback_model}")
                return await self.agenerate(messages, temperature, max_tokens, self.fallback_model)
            raise
        except Exception as e:
            logger.error(f"Groq async generation failed: {e}")
            raise


_groq_service: GroqService | None = None


def get_groq_service() -> GroqService:
    global _groq_service
    if _groq_service is None:
        _groq_service = GroqService()
    return _groq_service
