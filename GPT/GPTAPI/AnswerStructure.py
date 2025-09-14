from typing import List, Literal
from pydantic import BaseModel

class PlayerOption(BaseModel):
    id: Literal["G1", "G2", "B1", "B2"]
    type: Literal["good", "bad"]
    text_ru: str
    text_tt: str

class InitialOption(BaseModel):
    id: Literal["G1", "G2", "B1", "B2"]
    type: Literal["good", "bad"]
    text_ru: str
    text_tt: str

class BranchNode(BaseModel):
    npc_phrase_ru: str
    npc_phrase_tt: str
    options: List[PlayerOption]

class MultiBranchDialogue(BaseModel):
    initial_npc_phrase_ru: str
    initial_npc_phrase_tt: str
    initial_options: List[InitialOption]
    good_branches: List[BranchNode]
    bad_branches: List[BranchNode]

class EndingResult(BaseModel):
    npc_phrase_ru: str
    npc_phrase_tt: str
    final_text_ru: str
    final_text_tt: str
    story_ru: str
    story_tt: str
