from __future__ import annotations

from typing import Optional
from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession
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
    name: str,
    description: str | None = None,
    avatar_url: str | None = None,
):
    """Create a new character and persist it.

    Note: added for future use (seeding/admin flows).
    """
    character = Character(name=name, description=description, avatar_url=avatar_url)
    session.add(character)
    await session.commit()
    await session.refresh(character)
    return character
