import json
import os
import threading
from typing import Any
from app.core.logger import get_logger

logger = get_logger("services.local_store")

DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "data")
COMPLAINTS_FILE = os.path.join(DATA_DIR, "complaints.json")

_lock = threading.Lock()


def _ensure_dir():
    os.makedirs(DATA_DIR, exist_ok=True)


def _load_all() -> dict[str, dict]:
    _ensure_dir()
    if not os.path.exists(COMPLAINTS_FILE):
        return {}
    try:
        with open(COMPLAINTS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, OSError) as e:
        logger.warning(f"Failed to load complaints file: {e}")
        return {}


def _save_all(data: dict[str, dict]):
    _ensure_dir()
    tmp = COMPLAINTS_FILE + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, default=str)
    os.replace(tmp, COMPLAINTS_FILE)


def get_all() -> dict[str, dict]:
    with _lock:
        return _load_all()


def get(key: str) -> dict | None:
    with _lock:
        return _load_all().get(key)


def set(key: str, value: dict):
    with _lock:
        data = _load_all()
        data[key] = value
        _save_all(data)


def update(key: str, updates: dict):
    with _lock:
        data = _load_all()
        if key in data:
            data[key].update(updates)
            _save_all(data)


def delete(key: str) -> bool:
    with _lock:
        data = _load_all()
        if key in data:
            del data[key]
            _save_all(data)
            return True
        return False


def find(predicate) -> dict | None:
    with _lock:
        data = _load_all()
        for v in data.values():
            if predicate(v):
                return v
        return None


def find_all(predicate) -> list[dict]:
    with _lock:
        data = _load_all()
        return [v for v in data.values() if predicate(v)]
