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


class GenerateDialogueIn(BaseModel):
    style: str | None = Field(None, description="Стиль повествования")
    persona: str | None = Field(None, description="Характер и личность NPC")
    context: str = Field("", description="Контекст сцены/ситуации")


class GenerateEndingIn(BaseModel):
    style: str | None = Field(None, description="Стиль повествования")
    persona: str | None = Field(None, description="Характер и личность NPC")
    start_ru: str = Field("", description="Начало сцены (рус)")
    start_tt: str = Field("", description="Начало сцены (тат)")
    visited_summary_ru: list[str] = Field([""], description="Перечень пройденных блоков (рус)")
    visited_summary_tt: list[str] = Field([""], description="Перечень пройденных блоков (тат)")


class GenerateStoryAndDialogueIn(BaseModel):
    user_id: UUID = Field(..., description="ID пользователя")
    style: str | None = Field(None, description="Стиль повествования")
    persona: str | None = Field(None, description="Характер и личность NPC")
    persona_name: str | None = Field(None, description="Имя персонажа")
    context: str = Field("", description="Контекст сцены/ситуации")


class StoryWithDialogueOut(BaseModel):
    session: StorySessionOut
    dialogue: dict = Field(..., description="Сгенерированный узел диалога (MultiBranchDialogue)")
