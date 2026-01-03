
import json
import os

json_path = r"c:\Users\Administrator\ .gemini\antigravity\scratch\HearthstoneOne\data\cards.json".replace(" ", "")
with open(json_path, 'r', encoding='utf-8') as f:
    cards = json.load(f)

missing_ids = [
    "CORE_EX1_246", "TLC_222", "FIR_939", "TLC_623", "TIME_034", "TIME_750",
    "CORE_EX1_144", "CORE_EX1_145", "GDB_472", "CORE_TOY_100", "EDR_527", "DINO_407", "TIME_711", "TIME_712",
    "CORE_EX1_169", "CORE_EX1_169", "FIR_907", "BG31_BOB", "TIME_211t1", "TIME_211t2", "TIME_702",
    "GDB_456", "GDB_305", "TLC_220",
    "CORE_GVG_061", "TTN_908", "CORE_BT_292", "EDR_253", "TLC_438"
]

results = {}
for card in cards:
    card_id = card.get("id")
    if card_id in missing_ids:
        results[card_id] = {
            "name": card.get("name"),
            "text": card.get("text"),
            "set": card.get("set")
        }

with open("missing_info.json", "w") as out:
    json.dump(results, out, indent=2)
