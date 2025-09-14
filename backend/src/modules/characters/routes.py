from __future__ import annotations

from typing import List
from uuid import UUID

from fastapi import APIRouter, HTTPException

from src.modules.characters import repository as repo
from src.modules.characters.schemas import CharacterCreateIn, CharacterOut
from src.storages.sql.dependencies import DbSessionDep


router = APIRouter(prefix="/characters", tags=["characters"])


@router.get("", response_model=List[CharacterOut])
async def list_characters(session: DbSessionDep) -> List[CharacterOut]:
    characters = await repo.list_characters(session)
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
        "Создает персонажа с локализованным названием и деталями (JSON).\n"
        "Предназначено для будущего (админ/сидинг), не обязательно в текущем потоке."
    ),
)
async def create_character(
    data: CharacterCreateIn,
    session: DbSessionDep,
) -> CharacterOut:
    character = await repo.create_character(
        session,
        title=data.title.model_dump(),
        image=data.image,
        details=data.details.model_dump(),
    )
    return CharacterOut.model_validate(character, from_attributes=True)
