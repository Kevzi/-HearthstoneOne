import json
import os
import sys

# Add root to path
sys.path.append(os.getcwd())

from simulator.deck_generator import DeckGenerator
from hearthstone.deckstrings import parse_deckstring

def scan_decks():
    json_path = os.path.join("data", "meta_decks.json")
    if not os.path.exists(json_path):
        print("meta_decks.json not found")
        return

    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    print("Scanning for DBF:3 and DBF:0...")
    
    found = False
    for class_name, decks in data.items():
        for deck in decks:
            code = deck['code']
            name = deck['name']
            
            try:
                decoded = parse_deckstring(code)
                cards = decoded[0] # List of (dbf_id, count)
                hero_dbf = decoded[1] # Hero ID
                
                dbf_ids = [c[0] for c in cards]
                
                if 3 in dbf_ids:
                    print(f"FOUND DBF:3 in deck: '{name}' ({class_name})")
                    print(f"Code: {code}")
                    found = True
                    
                if 0 in dbf_ids:
                    print(f"FOUND DBF:0 in deck: '{name}' ({class_name})")
                    print(f"Code: {code}")
                    found = True
                    
            except Exception as e:
                print(f"Error decoding {name}: {e}")

    if not found:
        print("Strange... DBF:3 not found in deck lists. Is it a Hero ID?")

if __name__ == "__main__":
    scan_decks()
