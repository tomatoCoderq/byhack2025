from __future__ import annotations

from uuid import UUID
from pydantic import BaseModel, Field


class LocalizedText(BaseModel):
    ru: str
    tt: str


class CharacterDetails(BaseModel):
    history: LocalizedText
    habitat: LocalizedText
    features: LocalizedText


class CharacterOut(BaseModel):
    id: UUID
    title: LocalizedText
    image: str | None = Field(default=None)
    details: CharacterDetails


class CharacterCreateIn(BaseModel):
    title: LocalizedText
    image: str | None = Field(default=None)
    details: CharacterDetails

