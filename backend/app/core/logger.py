import logging
import json
import time
from typing import Any
from app.core.config import get_settings


class StructuredFormatter(logging.Formatter):
    """JSON structured log formatter."""

    def format(self, record: logging.LogRecord) -> str:
        log_entry = {
            "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S%z"),
            "level": record.levelname,
            "logger": record.name,
            "message": record.getMessage(),
        }
        if hasattr(record, "extra_data"):
            log_entry["data"] = record.extra_data
        if record.exc_info:
            log_entry["exception"] = self.formatException(record.exc_info)
        return json.dumps(log_entry, default=str)


def setup_logging() -> logging.Logger:
    settings = get_settings()
    logger = logging.getLogger("pharmaqms")
    logger.setLevel(getattr(logging, settings.LOG_LEVEL.upper(), logging.INFO))

    if not logger.handlers:
        console_handler = logging.StreamHandler()
        if settings.DEBUG:
            console_handler.setFormatter(logging.Formatter(settings.LOG_FORMAT))
        else:
            console_handler.setFormatter(StructuredFormatter())
        logger.addHandler(console_handler)

    logging.getLogger("uvicorn.access").setLevel(logging.WARNING)
    return logger


def get_logger(name: str) -> logging.Logger:
    return logging.getLogger(f"pharmaqms.{name}")


class PerformanceLogger:
    """Context manager for timing operations."""

    def __init__(self, operation: str, logger: logging.Logger):
        self.operation = operation
        self.logger = logger
        self.start_time = 0.0

    def __enter__(self):
        self.start_time = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        duration = time.time() - self.start_time
        extra = {
            "operation": self.operation,
            "duration_ms": round(duration * 1000, 2),
        }
        if exc_type:
            self.logger.error(f"{self.operation} failed in {duration:.3f}s: {exc_val}", extra={"extra_data": extra})
        else:
            self.logger.info(f"{self.operation} completed in {duration:.3f}s", extra={"extra_data": extra})
        return False
