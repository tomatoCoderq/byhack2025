from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.config import settings
from src.modules.users.routes import router as users_router
from src.modules.characters.routes import router as characters_router
from src.modules.stories.routes import router as stories_router

app = FastAPI(title="Backend API")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origin_regex=settings.cors_allow_origin_regex,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


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
