from __future__ import annotations

from uuid import UUID, uuid4

from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession


async def register_user(session: AsyncSession, name: str) -> UUID:
    """Create a user with a generated id and return it.

    Note: current schema has only `id` in `users` table, so `name` is not stored.
    """
    user_id = uuid4()
    await session.execute(text("INSERT INTO users VALUES (:id, :name)"), {"id": str(user_id), "name": name})
    await session.commit()
    return user_id


async def login_user(session: AsyncSession, name: str) -> UUID:
    """Find a user by name and return its id.

    Raises LookupError if no user with such name exists.
    """
    result = await session.execute(
        text("SELECT id FROM users WHERE name = :name LIMIT 1"), {"name": name}
    )
    row = result.first()
    if not row:
        raise LookupError("user-not-found")
    user_id = row[0]
    try:
        return user_id if isinstance(user_id, UUID) else UUID(str(user_id))
    except Exception:
        # Normalize any DB-driver specific return types to UUID
        return UUID(str(user_id))
