from __future__ import annotations

from uuid import UUID

from pydantic import BaseModel, Field


class NameIn(BaseModel):
    name: str = Field(..., description="Display name provided by the user")


class UserOut(BaseModel):
    id: UUID = Field(..., description="Generated user identifier (UUIDv4)")
    name: str = Field(..., description="Echo of the provided display name")
