from uuid import UUID
from sqlmodel import SQLModel

class CharacterOut(SQLModel):
    id: UUID
    name: str
    description: str | None = None
    avatar_url: str | None = None


class CharacterCreateIn(SQLModel):
    name: str
    description: str | None = None
    avatar_url: str | None = None
    

