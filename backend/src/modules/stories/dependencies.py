from __future__ import annotations

from fastapi import Depends
from openai import AsyncOpenAI

from GPT.GPTAPI import RequestAPI
from src.config import settings


def get_openai_client() -> AsyncOpenAI:
    """Provide an AsyncOpenAI client configured with project settings."""
    return AsyncOpenAI(api_key=settings.openai_api_key.get_secret_value())


def get_gpt_api(client: AsyncOpenAI = Depends(get_openai_client)) -> RequestAPI:
    """Provide a RequestAPI wrapper for GPT requests."""
    return RequestAPI(client, model="gpt-4o-mini")

