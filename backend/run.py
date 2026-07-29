import uvicorn
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))


def main():
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info",
    )


if __name__ == "__main__":
    main()
