from groq import Groq, APIConnectionError, APIStatusError, RateLimitError
from typing import Any, AsyncGenerator
from app.core.config import get_settings
from app.core.logger import get_logger
import time

logger = get_logger("services.llm")


class GroqService:
    """Service for interacting with Groq API using Gemma models."""

    def __init__(self):
        settings = get_settings()
        self.client = Groq(api_key=settings.GROQ_API_KEY)
        self.model = settings.GROQ_MODEL
        self.temperature = settings.GROQ_TEMPERATURE
        self.max_tokens = settings.GROQ_MAX_TOKENS

    def generate(
        self,
        messages: list[dict[str, str]],
        temperature: float | None = None,
        max_tokens: int | None = None,
    ) -> str:
        start = time.time()
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                temperature=temperature or self.temperature,
                max_tokens=max_tokens or self.max_tokens,
                top_p=0.9,
                stream=False,
            )
            content = response.choices[0].message.content
            elapsed = time.time() - start
            logger.info(
                f"Groq response generated in {elapsed:.3f}s "
                f"(tokens={response.usage.total_tokens if response.usage else 'N/A'})"
            )
            return content
        except RateLimitError as e:
            logger.error(f"Groq rate limit exceeded: {e}")
            raise
        except APIConnectionError as e:
            logger.error(f"Groq connection failed: {e}")
            raise
        except APIStatusError as e:
            logger.error(f"Groq API error {e.status_code}: {e.message}")
            raise
        except Exception as e:
            logger.error(f"Groq generation failed: {e}")
            raise

    async def agenerate(
        self,
        messages: list[dict[str, str]],
        temperature: float | None = None,
        max_tokens: int | None = None,
    ) -> str:
        start = time.time()
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                temperature=temperature or self.temperature,
                max_tokens=max_tokens or self.max_tokens,
                top_p=0.9,
                stream=False,
            )
            content = response.choices[0].message.content
            elapsed = time.time() - start
            logger.info(
                f"Groq async response generated in {elapsed:.3f}s "
                f"(tokens={response.usage.total_tokens if response.usage else 'N/A'})"
            )
            return content
        except RateLimitError as e:
            logger.error(f"Groq rate limit exceeded: {e}")
            raise
        except APIConnectionError as e:
            logger.error(f"Groq connection failed: {e}")
            raise
        except APIStatusError as e:
            logger.error(f"Groq API error {e.status_code}: {e.message}")
            raise
        except Exception as e:
            logger.error(f"Groq generation failed: {e}")
            raise
