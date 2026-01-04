import json
import os

# Sets currently in Arena Rotation (Jan 2026)
ARENA_SETS = [
    'THE_LOST_CITY',
    'TIME_TRAVEL',
    'EMERALD_DREAM',
    'SPACE',            # Likely "The Great Dark Beyond"
    'ISLAND_VACATION',  # Likely "Perils in Paradise"
    'WHIZBANGS_WORKSHOP',
    'CORE',
    'PATH_OF_ARTHAS'    # Often included for DK
]

OUTPUT_FILE = "data/arena_pool.json"

def generate_arena_pool():
    print("Loading database...")
    try:
        with open('data/cards.json', 'r', encoding='utf-8') as f:
            all_cards = json.load(f)
    except FileNotFoundError:
        print("Error: data/cards.json not found.")
        return

    arena_cards = []
    
    # Stats
    count_by_set = {s: 0 for s in ARENA_SETS}
    
    for card in all_cards:
        # 1. Filter by Set
        card_set = card.get('set')
        if card_set not in ARENA_SETS:
            continue
            
        # 2. Filter Types (Only playable cards)
        if card.get('type') not in ['MINION', 'SPELL', 'WEAPON', 'LOCATION', 'HERO']:
            continue
            
        # 3. Exclude Non-Collectible (Tokens, etc)
        # Usually cards have 'collectible': True. If missing, often it's a token.
        # But 'set' implies main set. Let's check keys.
        # Often checking for DbfId or rarity is a good proxy if 'collectible' key is missing.
        # Let's assume everything with a Rarity is draftable (Tokens usually have no rarity or FREE/COMMON hidden)
        if 'rarity' not in card:
            continue
            
        # 4. Exclude Quests if needed (Arena usually bans quests), but let's keep them for now.
        
        arena_cards.append(card)
        count_by_set[card_set] += 1

    print(f"Generating Arena Pool from {len(all_cards)} total cards...")
    print("-" * 30)
    for s in ARENA_SETS:
        print(f"{s}: {count_by_set[s]} cards")
    print("-" * 30)
    print(f"Total Arena Pool Size: {len(arena_cards)} cards")
    
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        json.dump(arena_cards, f, indent=4)
        
    print(f"Saved to {OUTPUT_FILE}")

if __name__ == "__main__":
    generate_arena_pool()
