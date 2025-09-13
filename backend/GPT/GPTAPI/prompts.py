from string import Template

multi_branch_prompt = Template("""
Ты — генератор диалоговых узлов для обучающей игры по татарскому языку.
Фразы должны быть простыми и короткими, понятными детям. Каждая фраза — на русском и татарском.

Характер NPC:
$persona

Сгенерируй один узел:
1) initial_npc_phrase_ru и initial_npc_phrase_tt.
   initial_options — ровно 4 ответа игрока:
     G1,G2: type="good"
     B1,B2: type="bad"
   У каждого ответа: text_ru и text_tt.

2) good_branches — ровно 2 ветви (good1, good2):
   npc_phrase_ru и npc_phrase_tt,
   options: 4 ответа игрока (G1,G2 good; B1,B2 bad), у каждого text_ru и text_tt.

3) bad_branches — ровно 2 ветви (bad1, bad2):
   npc_phrase_ru и npc_phrase_tt,
   options: 4 ответа игрока (G1,G2 good; B1,B2 bad), у каждого text_ru и text_tt.

Стиль: $style
Контекст: $context
Верни только данные по схеме MultiBranchDialogue.
""")

ending_prompt = Template("""
Ты — генератор финала детской истории на русском и татарском.
Фразы должны быть простыми и короткими, понятными детям.

Дано:
Начало сцены:
$start_ru
$start_tt

Пройденные блоки игрока (строго использовать для логики финала):
$visited_summary_ru
$visited_summary_tt

Сгенерируй:
npc_phrase_ru и npc_phrase_tt — короткая последняя реплика NPC
final_text_ru и final_text_tt — краткое общее описание финала, согласованное с перечисленными блоками

Стиль: $style
Характер NPC: $persona
Верни только данные по схеме EndingResult.
""")
