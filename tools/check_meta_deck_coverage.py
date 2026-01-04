import json
import os
import sys

# Paths
DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "data")
EFFECTS_DIR = os.path.join(os.path.dirname(__file__), "..", "card_effects")
META_DECKS_PATH = os.path.join(DATA_DIR, "meta_decks.json")

# Helpers
def load_json(path):
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

# Cached map of all implemented effects
_IMPLEMENTED_MAP = {}

def build_effect_map():
    global _IMPLEMENTED_MAP
    _IMPLEMENTED_MAP = {}
    for root, _, files in os.walk(EFFECTS_DIR):
        for f in files:
            if f.startswith("effect_") and f.endswith(".py"):
                card_id = f.replace("effect_", "").replace(".py", "")
                _IMPLEMENTED_MAP[card_id] = os.path.join(root, f)

def find_effect_file(card_id):
    # Case insensitive check
    for kid in _IMPLEMENTED_MAP:
        if kid.lower() == card_id.lower():
            return True
    return False

def main():
    build_effect_map()
    print("Loading Meta Decks...")
    try:
        meta_decks = load_json(META_DECKS_PATH)
    except FileNotFoundError:
        print("Error: data/meta_decks.json not found.")
        return

    # simple DB for names using data/cards.json if available
    card_db = {}
    try:
        cards_json = load_json(os.path.join(DATA_DIR, "cards.json"))
        for c in cards_json:
            card_db[c['id']] = c
    except:
        print("Warning: data/cards.json not found, showing IDs only.")

    from hearthstone.deckstrings import parse_deckstring
    
    overall_missing = set()

    print("\n=== META DECK COVERAGE REPORT ===\n")

    for class_name, decks in meta_decks.items():
        print(f"--- CLASS: {class_name} ---")
        for deck in decks:
            deck_name = deck['name']
            card_ids = []
            
            # Get card list
            if 'cards' in deck:
                card_ids = deck['cards']
            elif 'code' in deck:
                try:
                    decoded = parse_deckstring(deck['code'])
                    # decoded.cards is list of (dbf_id, count)
                    # We need to map DBF to ID. This requires the DB to be fully indexed.
                    # Since I don't want to reimplement the whole DB map here, 
                    # I will rely on the fact that if 'cards' isn't explicitly provided, 
                    # checking coverage is harder without the full simulation stack.
                    # BUT wait, the project usually has 'cards' lists in meta_decks.json OR use the simulator.
                    # Let's try to use simulator's DeckGenerator if possible?
                    # No, let's keep it simple. If I can't decode easily without DBF map, I'll alert.
                    
                    # Actually, I can build a quick DBF map from cards.json
                    pass 
                except:
                    print(f"  [!] Could not parse deckstring for {deck_name}")
                    continue
            
            # If we rely on deckstrings, we need the DBF map. 
            # If the user's meta_decks.json has 'cards' fields (lists of IDs), we are good.
            # Assuming 'cards' might be present or we skip.
            # Let's verify 'cards' presence.
            
            if not card_ids and 'code' in deck:
                # Build DBF map on the fly
                dbf_map = {}
                for cid, cdata in card_db.items():
                    if 'dbfId' in cdata:
                        dbf_map[cdata['dbfId']] = cid
                
                try:
                    decoded = parse_deckstring(deck['code'])
                    cards_list = decoded.cards if hasattr(decoded, 'cards') else decoded[0]
                    for dbf, count in cards_list:
                        if dbf in dbf_map:
                            card_ids.append(dbf_map[dbf])
                        else:
                            # Hero or unknown
                            pass
                except Exception as e:
                    print(f"  [Error decoding]: {e}")

            if not card_ids:
                print(f"  [?] {deck_name}: No card IDs found (decode failed or empty).")
                continue

            # CHECK COVERAGE
            missing = []
            implemented_count = 0
            # Unique cards check
            unique_ids = set(card_ids)
            
            for cid in unique_ids:
                # Is it simple keyword?
                cdata = card_db.get(cid, {})
                text = cdata.get('text', '')
                mechanics = cdata.get('mechanics', [])
                
                # Check file existence
                has_file = find_effect_file(cid)
                
                # Logic for "Is it implemented?":
                # 1. Has python file? YES.
                # 2. Is vanilla (no text)? YES (engine handles it).
                # 3. Only native keywords (Taunt, Rush...)? YES (engine handles it).
                
                is_vanilla = not text
                is_keyword_only = False
                
                # Simple keyword check (rough)
                import re
                keywords = ["Taunt", "Divine Shield", "Rush", "Charge", "Stealth", "Windfury", "Reborn", "Lifesteal", "Poisonous", "Elusive", "Titan", "Forge", "Tradeable", "Battlecry", "Deathrattle", "Combo", "Choose One", "Discover"]
                # If text contains ONLY supported keywords (processed by JSON mechanics), it's fine.
                # Actually, Titan, Forge, Battlecry DO need scripts usually.
                # Supported purely via JSON: Taunt, Divine Shield, Rush, Charge, Stealth, Windfury, Reborn, Lifesteal, Poisonous, Elusive.
                
                native_keywords = ["Taunt", "Divine Shield", "Rush", "Charge", "Stealth", "Windfury", "Reborn", "Lifesteal", "Poisonous", "Elusive"]
                
                # Remove HTML
                clean_text = re.sub(r'<[^>]+>', '', text).replace('[x]', '').strip()
                pass_text = clean_text
                for kw in native_keywords:
                    pass_text = re.sub(kw, '', pass_text, flags=re.IGNORECASE)
                pass_text = re.sub(r'[,.\s]', '', pass_text)
                
                if not pass_text and len(clean_text) > 0:
                     is_keyword_only = True
                
                if has_file or is_vanilla or is_keyword_only:
                    implemented_count += 1
                else:
                    missing.append((cid, cdata.get('name', cid)))
                    overall_missing.add((cid, cdata.get('name', cid)))

            total_unique = len(unique_ids)
            percent = (implemented_count / total_unique) * 100
            
            status = "[OK]" if percent == 100 else "[!]"
            if percent < 50: status = "[XX]"
            
            print(f"  {status} {deck_name:30} : {percent:5.1f}% ({len(missing)} missing)")
            if missing:
                # Show top 3 missing
                print(f"     Missing: {', '.join([m[1] for m in missing[:3]])} ...")

    print("\n=== TOTAL UNIQUE MISSING CARDS IN META ===")
    print(f"Count: {len(overall_missing)}")
    # for cid, name in sorted(list(overall_missing))[:10]:
    #     print(f" - {name} ({cid})")

if __name__ == "__main__":
    main()
