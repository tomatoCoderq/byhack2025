import src.logging_  # noqa

from fastapi import FastAPI
from fastapi.exception_handlers import http_exception_handler
from fastapi.exceptions import RequestValidationError
from fastapi.requests import Request
from fastapi.responses import PlainTextResponse
from fastapi_swagger import patch_fastapi
from pydantic import ValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException
from starlette.middleware.cors import CORSMiddleware

from src.logging_ import logger
from src.api import docs
from src.api.lifespan import lifespan
from src.config import settings

app = FastAPI(
    title=docs.TITLE,
    summary=docs.SUMMARY,
    description=docs.DESCRIPTION,
    version=docs.VERSION,
    contact=docs.CONTACT_INFO,
    license_info=docs.LICENSE_INFO,
    openapi_tags=docs.TAGS_INFO,
    servers=[
        {"url": settings.app_root_path, "description": "Current"},
    ],
    root_path=settings.app_root_path,
    root_path_in_servers=False,
    lifespan=lifespan,
    docs_url=None,
    redoc_url=None,
    swagger_ui_oauth2_redirect_url=None,
)
patch_fastapi(app)


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    """
    Log validation errors and return human-readable error message.
    Based on https://github.com/dantetemplar/fastapi-how-to-log#exceptions
    """
    as_validation_error = ValidationError.from_exception_data(
        str(request.url.path),
        line_errors=exc.errors(),  # type: ignore
    )
    error_str = str(as_validation_error)
    logger.warning(error_str, exc_info=False)
    return PlainTextResponse(error_str, status_code=422)


@app.exception_handler(StarletteHTTPException)
async def custom_http_exception_handler(request: Request, exc: StarletteHTTPException):
    """
    Log raised HTTPException.
    Based on https://github.com/dantetemplar/fastapi-how-to-log#exceptions
    """
    logger.warning(exc, exc_info=exc)
    return await http_exception_handler(request, exc)


app.add_middleware(
    CORSMiddleware,
    allow_origin_regex=settings.cors_allow_origin_regex,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Import routers above and include them below [do not edit this comment]
# Example router imports:
# from src.modules.users.routes import router as router_users
# app.include_router(router_users)
# ^