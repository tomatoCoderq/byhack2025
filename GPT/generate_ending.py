import os
import asyncio
import json
from dotenv import load_dotenv
from openai import AsyncOpenAI
from GPTAPI import RequestAPI, StoryMultiBranch, StoryEnding

PLAYER_PATH = [("good", 0), ("good", 1)]

def tone_from_path(path: list) -> str:
    goods = sum(1 for t, _ in path if t == "good")
    bads = sum(1 for t, _ in path if t == "bad")
    if goods == 2:
        return "good"
    if bads == 2:
        return "bad"
    return "mixed"

async def main():
    load_dotenv()
    client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    api = RequestAPI(client, model="gpt-4o-mini")

    req_dialog = StoryMultiBranch(
        style="сказочное фэнтези для детей",
        persona="Шурале — лесной дух: хитрый, насмешливый, любит щекотать путников. Говорит простыми словами."
    )
    dialog = await api.get_request(
        req_dialog,
        data="Игрок встречает Шурале в лесу у старого дуба ночью."
    )

    start_ru = dialog.initial_npc_phrase_ru
    start_tt = dialog.initial_npc_phrase_tt

    chosen_ru, chosen_tt = [], []

    for branch_type, idx in PLAYER_PATH:
        if branch_type == "good" and 0 <= idx < len(dialog.good_branches):
            chosen_ru.append(dialog.good_branches[idx].npc_phrase_ru)
            chosen_tt.append(dialog.good_branches[idx].npc_phrase_tt)
        elif branch_type == "bad" and 0 <= idx < len(dialog.bad_branches):
            chosen_ru.append(dialog.bad_branches[idx].npc_phrase_ru)
            chosen_tt.append(dialog.bad_branches[idx].npc_phrase_tt)

    visited_ru = " | ".join(chosen_ru)
    visited_tt = " | ".join(chosen_tt)
    tone = tone_from_path(PLAYER_PATH)

    req_end = StoryEnding(
        style="сказочное фэнтези для детей",
        persona=req_dialog.persona,
        start_ru=start_ru,
        start_tt=start_tt,
        visited_summary_ru=visited_ru,
        visited_summary_tt=visited_tt,
        tone_plan=tone,
    )

    ending = await api.get_request(req_end, data="")
    print(json.dumps(ending.model_dump(), ensure_ascii=False, indent=2))

if __name__ == "__main__":
    asyncio.run(main())
