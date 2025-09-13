import os
import asyncio
import json
from dotenv import load_dotenv
from openai import AsyncOpenAI
from GPTAPI import RequestAPI, StoryMultiBranch, StoryEnding  # замените yourpkg на ваш пакет

GOOD_INDEX = 1  # good2
BAD_INDEX = 0   # bad1

def tone_from_choices(good_chosen: bool, bad_chosen: bool) -> str:
    if good_chosen and bad_chosen:
        return "mixed"
    if good_chosen and not bad_chosen:
        return "good"
    if bad_chosen and not good_chosen:
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
    good_branches = dialog.good_branches or []
    bad_branches = dialog.bad_branches or []

    good_chosen = 0 <= GOOD_INDEX < len(good_branches)
    bad_chosen = 0 <= BAD_INDEX < len(bad_branches)

    if good_chosen:
        chosen_ru.append(good_branches[GOOD_INDEX].npc_phrase_ru)
        chosen_tt.append(good_branches[GOOD_INDEX].npc_phrase_tt)
    if bad_chosen:
        chosen_ru.append(bad_branches[BAD_INDEX].npc_phrase_ru)
        chosen_tt.append(bad_branches[BAD_INDEX].npc_phrase_tt)

    visited_ru = " | ".join(chosen_ru)
    visited_tt = " | ".join(chosen_tt)
    tone = tone_from_choices(good_chosen, bad_chosen)

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
