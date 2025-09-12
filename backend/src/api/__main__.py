import os
import sys

try:
    import uvicorn  # type: ignore
except Exception:
    print(
        "Uvicorn is required to run the API server.\n"
        "Install it with: pip install uvicorn[standard]",
        file=sys.stderr,
    )
    raise


def main() -> None:
    host = os.getenv("HOST", "0.0.0.0")
    port = int(os.getenv("PORT", "8000"))
    reload = os.getenv("RELOAD", "true").lower() in {"1", "true", "yes", "on"}
    # IMPORTANT: pass the application as an import string so reload/workers work
    app_path = os.getenv("APP", "src.api.app:app")
    uvicorn.run(app_path, host=host, port=port, reload=reload)


if __name__ == "__main__":
    main()
