from __future__ import annotations

from uuid import UUID

from fastapi import APIRouter, Body, HTTPException, Query, Depends

from src.modules.stories import repository as repo
from src.modules.stories.schemas import (
    StorySessionOut,
    StorySessionStatusUpdateIn,
    GenerateDialogueIn,
    GenerateEndingIn,
    GenerateStoryAndDialogueIn,
    StoryWithDialogueOut,
)
from src.storages.sql.dependencies import DbSessionDep
from src.modules.stories.dependencies import get_gpt_api
from GPT.GPTAPI import (
    StoryMultiBranch,
    StoryEnding,
    MultiBranchDialogue,
    EndingResult,
    RequestAPI,
)
from src.modules.characters.repository import (
    get_any_character_id,
    get_character_id_by_name,
)


router = APIRouter(prefix="/stories", tags=["stories"])

# Здесь будет использован модуль для взаимодействия с API openAI, так что дополнительно будет возвращаться полная история, сгенерированная гпт


@router.post(
    "",
    response_model=StoryWithDialogueOut,
    status_code=201,
    summary="Создать сессию и сгенерировать диалог",
    description="Объединенный эндпоинт: принимает user_id, style, persona, context; создает запись в БД и возвращает сгенерированный диалог.",
)
async def create_story_and_generate_dialogue(
    data: GenerateStoryAndDialogueIn = Body(...),
    session: DbSessionDep = None,  # type: ignore
    gpt: RequestAPI = Depends(get_gpt_api),
) -> StoryWithDialogueOut:
    # resolve character by name if provided, otherwise pick any existing
    character_id = None
    if getattr(data, "persona_name", None):
        # type: ignore[arg-type]
        character_id = await get_character_id_by_name(session, data.persona_name) # type: ignore
        if character_id is None:
            raise HTTPException(status_code=404, detail="Character not found")
    if character_id is None:
        character_id = await get_any_character_id(session)
    if character_id is None:
        raise HTTPException(
            status_code=409, detail="No characters available. Create a character first.")

    # persist story session
    entity = await repo.create_story_session(
        session, user_id=data.user_id, character_id=character_id
    )

    # generate dialogue via GPT
    req = StoryMultiBranch(
        style=data.style or "сказочное фэнтези",
        persona=data.persona or (
            "Шурале — лесной дух: хитрый, насмешливый, любит щекотать путников."
        ),
    )
    dialogue = await gpt.get_request(req, data=data.context)

    return StoryWithDialogueOut(
        session=StorySessionOut.model_validate(entity, from_attributes=True),
        dialogue=dialogue.model_dump() if hasattr( # type: ignore
            dialogue, "model_dump") else dialogue,  # type: ignore
    )


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

@router.post(
    "/generate/ending",
    response_model=EndingResult,
    summary="Сгенерировать финал истории",
)
async def generate_ending(
    data: GenerateEndingIn = Body(...),
    gpt: RequestAPI = Depends(get_gpt_api),
):
    req = StoryEnding(
        style=data.style or "сказочное фэнтези",
        persona=data.persona or (
            "Шурале — лесной дух: хитрый, насмешливый, любит щекотать путников."
        ),
        start_ru=data.start_ru,
        start_tt=data.start_tt,
        visited_summary_ru=[f"{v}\n" for v in data.visited_summary_ru][0],
        visited_summary_tt=[f"{v}\n" for v in data.visited_summary_tt][0],
    )
    result = await gpt.get_request(req, data="")
    return result
