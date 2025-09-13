from __future__ import annotations


from fastapi import APIRouter

from src.modules.users import repository as repo
from src.storages.sql.dependencies import DbSessionDep
from src.modules.users.schemas import NameIn, UserOut


router = APIRouter(
    prefix="/users",
    tags=["users"],
)


@router.post(

    "/register",
    response_model=UserOut,
    status_code=201,
    summary="Register a new user",
    description=(
        "Creates a new user identifier for the provided display name.\n\n"
        "Note: in this demo, only the generated ID is persisted; the name is not stored."
    ),
    response_description="The created user identifier with the provided name.",
    responses={
        201: {
            "description": "User registered successfully",
            "content": {
                "application/json": {
                    "example": {
                        "id": "f3a7b2e1-9a3b-4ef7-9b36-9d0f2a1a6a2c",
                        "name": "Alice",
                    }
                }
            },
        }
    },
)
async def register(
    data: NameIn,
    session: DbSessionDep,
) -> UserOut:
    user_id = await repo.register_user(session, data.name)
    return UserOut(id=user_id, name=data.name)


@router.post(
    "/login",
    response_model=UserOut,
    summary="Login with name (demo)",
    description=(
        "Accepts a display name and returns a newly generated identifier.\n\n"
        "This is a simplified demo flow and does not validate or persist users."
    ),
    response_description="A generated identifier with the provided name.",
    responses={
        200: {
            "description": "Logged in (demo)",
            "content": {
                "application/json": {
                    "example": {
                        "id": "c9f1d3e2-4b64-4b3f-9e2f-0b2a6c1d2f3a",
                        "name": "Alice",
                    }
                }
            },
        }
    },
)
async def login(
    data: NameIn,
    session: DbSessionDep,
) -> UserOut:
    user_id = await repo.login_user(session, data.name)
    return UserOut(id=user_id, name=data.name)
