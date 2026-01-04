from hearthstone.deckstrings import parse_deckstring
import json
import os

# 1. Build DBF -> ID map
dbf_map = {}
with open('data/cards.json', 'r', encoding='utf-8') as f:
    cards_data = json.load(f)
    for c in cards_data:
        if 'dbfId' in c:
            dbf_map[c['dbfId']] = c['id']

# 2. Load Meta Decks
with open('data/meta_decks.json', 'r', encoding='utf-8') as f:
    meta_decks = json.load(f)

# 3. Collect ALL IDs used in Meta Decks
all_meta_ids = set()
for cls, decks in meta_decks.items():
    for deck in decks:
        if 'cards' in deck:
            all_meta_ids.update(deck['cards'])
        elif 'code' in deck:
            try:
                decoded = parse_deckstring(deck['code'])
                cards_list = decoded.cards if hasattr(decoded, 'cards') else decoded[0]
                for dbf, count in cards_list:
                    if dbf in dbf_map:
                        all_meta_ids.add(dbf_map[dbf])
            except: pass

# 4. Check which files exist (case insensitive)
implemented = set()
for root, _, files in os.walk('card_effects'):
    for f in files:
        if f.startswith("effect_") and f.endswith(".py"):
            implemented.add(f.replace("effect_", "").replace(".py", "").upper())

missing = []
for mid in all_meta_ids:
    if mid.upper() not in implemented:
        # Check if it's vanilla or keyword only
        # (This logic is usually in the report, but here we want to list them for implementation)
        missing.append(mid)

print("TOTAL MISSING IDs in Meta Decks:")
for m in sorted(missing):
    # Get text
    text = "Unknown"
    for c in cards_data:
        if c['id'] == m:
            text = c.get('text', '')
            break
    print(f"- {m}: {text[:60]}")
