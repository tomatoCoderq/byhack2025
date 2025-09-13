from __future__ import annotations

from typing import List
from uuid import UUID

from fastapi import APIRouter, HTTPException, Body
from pydantic import BaseModel
from sqlmodel import SQLModel

# from src.modules.characters.schemas import CharacterCreateIn, CharacterOut
from src.modules.characters import repository as repo
from src.storages.sql.dependencies import DbSessionDep


router = APIRouter(prefix="/characters", tags=["characters"])


class CharacterOut(SQLModel):
    id: UUID
    name: str
    description: str | None = None
    avatar_url: str | None = None


class CharacterCreateIn(SQLModel):
    name: str
    description: str | None = None
    avatar_url: str | None = None


@router.get("", response_model=List[CharacterOut])
async def list_characters(session: DbSessionDep) -> List[CharacterOut]:
    characters = await repo.list_characters(session)
    print("getet", characters)
    return [CharacterOut.model_validate(c, from_attributes=True) for c in characters]


@router.get("/{character_id}", response_model=CharacterOut)
async def get_character(character_id: UUID, session: DbSessionDep) -> CharacterOut:
    character = await repo.get_character(session, character_id)
    if not character:
        raise HTTPException(status_code=404, detail="Character not found")
    return CharacterOut.model_validate(character, from_attributes=True)


@router.post(
    "",
    response_model=CharacterOut,
    status_code=201,
    summary="Create character (future use)",
    description=(
        "Creates a new character. This endpoint is intended for future use,\n"
        "such as admin tooling or initial seeding; it is not required for the\n"
        "current user flow."
    ),
)
async def create_character(
    data: CharacterCreateIn,
    session: DbSessionDep,
) -> CharacterOut:
    character = await repo.create_character(
        session,
        name=data.name,
        description=data.description,
        avatar_url=data.avatar_url,
    )
    return CharacterOut.model_validate(character, from_attributes=True)
