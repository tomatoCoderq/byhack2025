from __future__ import annotations

from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, Field

from src.storages.sql.models import StorySessionStatus


class StorySessionCreateIn(BaseModel):
    user_id: UUID = Field(..., description="ID of the user starting the session")
    character_id: UUID = Field(..., description="ID of the character involved")


class StorySessionStatusUpdateIn(BaseModel):
    status: StorySessionStatus = Field(..., description="New status for the session")


class StorySessionOut(BaseModel):
    id: UUID
    user_id: UUID
    character_id: UUID
    created_at: datetime
    status: StorySessionStatus

