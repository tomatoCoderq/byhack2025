from __future__ import annotations

from typing import Sequence
from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import select

from src.storages.sql.models import StorySession, StorySessionStatus


async def create_story_session(
    session: AsyncSession,
    *,
    user_id: UUID,
    character_id: UUID,
) -> StorySession:
    entity = StorySession(user_id=user_id, character_id=character_id)
    session.add(entity)
    await session.commit()
    await session.refresh(entity)
    return entity


async def list_story_sessions(
    session: AsyncSession,
    *,
    user_id: UUID | None = None,
) -> Sequence[StorySession]:
    stmt = select(StorySession)
    if user_id is not None:
        stmt = stmt.where(StorySession.user_id == user_id)
    result = await session.execute(stmt)
    return result.scalars().all()


async def get_story_session(session: AsyncSession, *, session_id: UUID) -> StorySession | None:
    return await session.get(StorySession, session_id)


async def update_story_session_status(
    session: AsyncSession,
    *,
    session_id: UUID,
    status: StorySessionStatus,
) -> StorySession | None:
    entity = await session.get(StorySession, session_id)
    if not entity:
        return None
    entity.status = status
    session.add(entity)
    await session.commit()
    await session.refresh(entity)
    return entity


async def delete_story_session(session: AsyncSession, *, session_id: UUID) -> bool:
    entity = await session.get(StorySession, session_id)
    if not entity:
        return False
    await session.delete(entity)
    await session.commit()
    return True

