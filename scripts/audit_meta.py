import os
import sys
import json

# Ensure project root is in path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from simulator import CardDatabase
from card_generator.cache import EffectCache

def audit_meta_decks():
    cache = EffectCache()
    db = CardDatabase.get_instance()
    db.load()
    
    with open("data/meta_decks.json", "r") as f:
        meta_decks = json.load(f)
        
    for class_name, decks in meta_decks.items():
        print(f"\n=== {class_name} ===")
        for deck in decks:
            print(f"Deck: {deck['name']}")
            # Decks can have 'code' or 'cards'
            cards_ids = []
            if 'cards' in deck:
                cards_ids = deck['cards']
            elif 'code' in deck:
                # We should have a deck decoder, but let's assume we can't easily decode here
                # and skip for now unless we have a helper
                print("  (Deck code - skipping detail)")
                continue
                
            for cid in cards_ids:
                data = db._cards.get(cid)
                if not data:
                    print(f"  [?] {cid} - Unknown")
                    continue
                
                status = "MISSING"
                if cache.is_cached(cid, data.card_set):
                    status = "OK"
                    # Check if it's a simplification
                    path = cache.get_effect_path(cid, data.card_set)
                    with open(path, "r", encoding="utf-8") as f_eff:
                        content = f_eff.read()
                        if "draw(1)" in content and len(content) < 200:
                            status = "SIMPLIFIED"
                        elif "pass" in content and len(content) < 150:
                            status = "PLACEHOLDER"
                
                print(f"  [{status}] {cid} - {data.name}")

if __name__ == "__main__":
    audit_meta_decks()
