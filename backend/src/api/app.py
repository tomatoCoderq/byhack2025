from fastapi import FastAPI

app = FastAPI(title="Backend API")


@app.get("/", tags=["system"])
def root():
    return {"message": "API is up"}


@app.get("/health", tags=["system"])
def health():
    return {"status": "ok"}
