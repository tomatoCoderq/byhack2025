import os
import asyncio
import json
from dotenv import load_dotenv
from openai import AsyncOpenAI
from GPTAPI import RequestAPI, StoryEnding

good_index = 0
bad_index = 1

async def main():
    load_dotenv()
    client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    api = RequestAPI(client, model="gpt-4o-mini")

    # пример данных: в реальности их нужно взять из результата диалога
    start_ru = "Эй, путник, куда спешишь в тёмный лес?"
    start_tt = "Әй, юлчы, караңгы урманга кая ашыгасың?"
    chosen_ru = ["Хочешь, я покажу тропинку?", "Ах, ты грубый, тогда я рассержусь!"]
    chosen_tt = ["Телисеңме, сукмакны күрсәтим?", "Әй, дорсалар, мин ачуланам!"]

    visited_ru = " | ".join(chosen_ru)
    visited_tt = " | ".join(chosen_tt)

    req = StoryEnding(
        style="сказочное фэнтези для детей",
        persona="Шурале — лесной дух: хитрый, насмешливый, любит щекотать путников. Говорит простыми словами.",
        start_ru=start_ru,
        start_tt=start_tt,
        visited_summary_ru=visited_ru,
        visited_summary_tt=visited_tt,
    )

    ending = await api.get_request(req, data="")
    print(json.dumps(ending.model_dump(), ensure_ascii=False, indent=2)) # type: ignore

if __name__ == "__main__":
    asyncio.run(main())
