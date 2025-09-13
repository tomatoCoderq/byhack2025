from __future__ import annotations

from uuid import UUID

from fastapi import APIRouter, Body, HTTPException, Query

from src.modules.stories import repository as repo
from src.modules.stories.schemas import (
    StorySessionCreateIn,
    StorySessionOut,
    StorySessionStatusUpdateIn,
)
from src.storages.sql.dependencies import DbSessionDep


router = APIRouter(prefix="/stories", tags=["stories"])

#Здесь будет использован модуль для взаимодействия с API openAI, так что дополнительно будет возвращаться полная история, сгенерированная гпт
@router.post(
    "",
    response_model=StorySessionOut,
    status_code=201,
    summary="Start a story session",
)
async def create_story_session(
    data: StorySessionCreateIn = Body(...),
    session: DbSessionDep = None, # type: ignore
) -> StorySessionOut:
    entity = await repo.create_story_session(
        session, user_id=data.user_id, character_id=data.character_id
    )
    return StorySessionOut.model_validate(entity, from_attributes=True)


@router.get(
    "",
    response_model=list[StorySessionOut],
    summary="List story sessions",
)
async def list_story_sessions(
    session: DbSessionDep,
    user_id: UUID | None = Query(None, description="Filter by user_id"),
) -> list[StorySessionOut]:
    items = await repo.list_story_sessions(session, user_id=user_id)
    return [StorySessionOut.model_validate(i, from_attributes=True) for i in items]


@router.get(
    "/{session_id}",
    response_model=StorySessionOut,
    summary="Get story session",
)
async def get_story_session(session_id: UUID, session: DbSessionDep) -> StorySessionOut:
    entity = await repo.get_story_session(session, session_id=session_id)
    if not entity:
        raise HTTPException(status_code=404, detail="Story session not found")
    return StorySessionOut.model_validate(entity, from_attributes=True)


@router.patch(
    "/{session_id}",
    response_model=StorySessionOut,
    summary="Update story session status",
)
async def update_story_session(
    session_id: UUID,
    data: StorySessionStatusUpdateIn,
    session: DbSessionDep,
) -> StorySessionOut:
    entity = await repo.update_story_session_status(
        session, session_id=session_id, status=data.status
    )
    if not entity:
        raise HTTPException(status_code=404, detail="Story session not found")
    return StorySessionOut.model_validate(entity, from_attributes=True)


# @router.delete(
#     "/{session_id}",
#     status_code=204,
#     summary="Delete story session",
# )
# async def delete_story_session(session_id: UUID, session: DbSessionDep) -> None:
#     ok = await repo.delete_story_session(session, session_id=session_id)
#     if not ok:
#         raise HTTPException(status_code=404, detail="Story session not found")
#     return None

