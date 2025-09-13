import os
import asyncio
import json
from dotenv import load_dotenv
from openai import AsyncOpenAI
from GPTAPI import RequestAPI, StoryMultiBranch

async def main():
    load_dotenv()
    client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    api = RequestAPI(client, model="gpt-4o-mini")
    req = StoryMultiBranch(
        style="сказочное фэнтези для детей",
        persona="Шурале — лесной дух: хитрый, насмешливый, любит щекотать путников. Говорит простыми словами."
    )
    dialog = await api.get_request(
        req,
        data="Игрок встречает Шурале в лесу у старого дуба ночью."
    )
    print(json.dumps(dialog.model_dump(), ensure_ascii=False, indent=2))

if __name__ == "__main__":
    asyncio.run(main())
