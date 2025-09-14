from __future__ import annotations

from typing import Optional
from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text
from sqlmodel import select

from src.storages.sql.models import Character


async def list_characters(session: AsyncSession):
    result = await session.execute(select(Character))
    return result.scalars().all()


async def get_character(session: AsyncSession, character_id: UUID) -> Optional[Character]:
    return await session.get(Character, character_id)


async def create_character(
    session: AsyncSession,
    *,
    title: dict,
    image: str | None,
    details: dict,
):
    """Create a new character with nested fields and persist it."""
    character = Character(title=title, image=image, details=details) # type: ignore
    session.add(character)
    await session.commit()
    await session.refresh(character)
    return character


async def get_any_character_id(session: AsyncSession) -> UUID | None:
    """Return the id of any existing character or None if table is empty."""
    result = await session.execute(select(Character.id).limit(1))
    return result.scalars().first()


async def get_character_id_by_name(session: AsyncSession, name: str) -> UUID | None:
    """Return character id by its localized title (ru/tt) or None if not found.

    Note: Uses PostgreSQL JSON operator ->> to compare string values.
    """
    res = await session.execute(
        text("""
            SELECT id
            FROM characters
            WHERE title->>'ru' = :name OR title->>'tt' = :name
            LIMIT 1
        """),
        {"name": name},
    )
    row = res.first()
    return row[0] if row else None
