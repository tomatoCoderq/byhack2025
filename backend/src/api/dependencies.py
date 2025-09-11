__all__ = ["api_key_dep", "ApiKeyDep"]

from typing import Annotated

from fastapi import Depends
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from src.api.exceptions import IncorrectCredentialsException
from src.config import settings

api_bearer_scheme = HTTPBearer(
    scheme_name="Bearer",
    description="Secret key for accessing API by external services",
    bearerFormat="JWT",
    auto_error=False,  # We'll handle error manually
)


def api_key_dep(
    bearer: HTTPAuthorizationCredentials | None = Depends(api_bearer_scheme),
) -> str:
    token = bearer and bearer.credentials
    if not token:
        raise IncorrectCredentialsException(no_credentials=True)
    if token != settings.api_key.get_secret_value():
        raise IncorrectCredentialsException(no_credentials=False)
    return token


ApiKeyDep = Annotated[str, Depends(api_key_dep)]
"""
Dependency for checking if the request is coming from an authorized external service.
"""