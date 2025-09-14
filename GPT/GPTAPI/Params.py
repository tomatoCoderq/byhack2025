from dataclasses import dataclass
from .AnswerStructure import MultiBranchDialogue, EndingResult
from .prompts import multi_branch_prompt, ending_prompt

@dataclass
class StoryMultiBranch:
    style: str = "сказочное фэнтези"
    persona: str = "Шурале — лесной дух: хитрый, насмешливый, любит щекотать путников."
    type: str = "storyMultiBranch"
    structure = MultiBranchDialogue
    async def comb(self, context: str = ""):
        return {
            "role": "system",
            "content": multi_branch_prompt.substitute(
                style=self.style,
                persona=self.persona,
                context=context or "—",
            )
        }

@dataclass
class StoryEnding:
    style: str = "сказочное фэнтези"
    persona: str = "Шурале — лесной дух: хитрый, насмешливый, любит щекотать путников."
    type: str = "storyEnding"
    structure = EndingResult
    start_ru: str = ""
    start_tt: str = ""
    visited_summary_ru: str = ""
    visited_summary_tt: str = ""
    tone_plan: str = "mixed"
    async def comb(self, context: str = ""):
        return {
            "role": "system",
            "content": ending_prompt.substitute(
                style=self.style,
                persona=self.persona,
                start_ru=self.start_ru or "—",
                start_tt=self.start_tt or "—",
                visited_summary_ru=self.visited_summary_ru or "—",
                visited_summary_tt=self.visited_summary_tt or "—",
                tone_plan=self.tone_plan,
            )
        }
