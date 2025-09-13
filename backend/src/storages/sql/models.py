from __future__ import annotations

from enum import StrEnum
import uuid
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, ConfigDict



from sqlmodel import Field, SQLModel
from sqlalchemy import Column, JSON

# from src.storages.sql.enums import StorySessionStatus
from sqlmodel._compat import SQLModelConfig
from typing import cast

def utcnow() -> datetime:
    return datetime.utcnow()

class StorySessionStatus(StrEnum):
    active = "active"
    completed = "completed"
    cancelled = "cancelled"

class Base(SQLModel):
    model_config = cast(SQLModelConfig, ConfigDict(json_schema_serialization_defaults_required=True))


class User(Base, table=True):
    __tablename__ = "users"  # type: ignore

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    name: str = Field(index=True, max_length=255)


class LocalizedText(BaseModel):
    ru: str
    tt: str


class CharacterDetails(BaseModel):
    history: LocalizedText
    habitat: LocalizedText
    features: LocalizedText


class Character(Base, table=True):
    __tablename__ = "characters"  # type: ignore

    # UUID primary key
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)

    # New structure fields
    title: LocalizedText = Field(sa_column=Column(JSON, nullable=False))
    image: Optional[str] = Field(default=None, max_length=2048)
    details: CharacterDetails = Field(sa_column=Column(JSON, nullable=False))


class StorySession(Base, table=True):
    __tablename__ = "story_sessions"  # type: ignore

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    user_id: uuid.UUID = Field(foreign_key="users.id")
    character_id: uuid.UUID = Field(foreign_key="characters.id")
    created_at: datetime = Field(default_factory=utcnow)
    status: StorySessionStatus = Field(default=StorySessionStatus.active)

#     # Relations
#     character: Optional["Character"] = Relationship(
#         back_populates="story_sessions",
#         sa_relationship_kwargs={"lazy": "selectin"},
#     )
