from fastapi import FastAPI
from src.modules.users.routes import router as users_router
from src.modules.characters.routes import router as characters_router
from src.modules.stories.routes import router as stories_router

app = FastAPI(title="Backend API")


@app.get("/", tags=["system"])
def root():
    return {"message": "API is up"}


@app.get("/health", tags=["system"])
def health():
    return {"status": "ok"}

# Routers
app.include_router(users_router)
app.include_router(characters_router)
app.include_router(stories_router)
