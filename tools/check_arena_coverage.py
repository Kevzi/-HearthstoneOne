import json
import os
import glob

ARENA_POOL = "data/arena_pool.json"
EFFECTS_DIR = "card_effects"

def check_coverage():
    print("Loading Arena Pool...")
    try:
        with open(ARENA_POOL, 'r', encoding='utf-8') as f:
            pool = json.load(f)
    except FileNotFoundError:
        print("Run scripts/generate_arena_pool.py first!")
        return

    # 1. Index implemented effects
    print(f"Scanning {EFFECTS_DIR} for implementations...")
    implemented_ids = set()
    
    # Walk recursively
    for root, dirs, files in os.walk(EFFECTS_DIR):
        for file in files:
            if file.startswith("effect_") and file.endswith(".py"):
                # Extract ID: effect_CORE_123.py -> CORE_123
                card_id = file.replace("effect_", "").replace(".py", "")
                implemented_ids.add(card_id)
                # Handle variants (t1, t2) if strict matching fails? 
                # For now assumes exact filename match to ID.

    # 2. Compare
    missing = []
    by_set = {}
    
    for card in pool:
        cid = card['id']
        cset = card.get('set', 'UNKNOWN')
        
        if cset not in by_set:
            by_set[cset] = {'total': 0, 'implemented': 0}
            
        by_set[cset]['total'] += 1
        
        if cid in implemented_ids:
            by_set[cset]['implemented'] += 1
        else:
            missing.append(card)

    # 3. Report
    print("\n=== ARENA COVERAGE REPORT ===")
    total_implemented = sum(s['implemented'] for s in by_set.values())
    total_cards = len(pool)
    print(f"Global Coverage: {total_implemented}/{total_cards} ({total_implemented/total_cards*100:.1f}%)")
    
    print("\nBy Set:")
    for sname, stats in by_set.items():
        pct = stats['implemented'] / stats['total'] * 100 if stats['total'] > 0 else 0
        print(f"  {sname:<20}: {stats['implemented']:>3}/{stats['total']:<3} ({pct:.1f}%)")
        
    print("\n=== MISSING HIGH PRIORITY CARDS (Top 10 Neutrals) ===")
    neutrals = [c for c in missing if c.get('cardClass') == 'NEUTRAL']
    # Sort by cost (low cost cards are foundational)
    neutrals.sort(key=lambda x: x.get('cost', 0))
    
    for c in neutrals[:10]:
        print(f"- [{c.get('id')}] {c.get('name')} ({c.get('cost')} mana) - {c.get('text', '')[:50]}...")

    print("\n=== MISSING LEGENDARIES (Top 10) ===")
    legends = [c for c in missing if c.get('rarity') == 'LEGENDARY']
    legends.sort(key=lambda x: x.get('cardClass', ''))
    
    for c in legends[:10]:
        print(f"- [{c.get('id')}] ({c.get('cardClass')}) {c.get('name')} - {c.get('text', '')[:50]}...")

if __name__ == "__main__":
    check_coverage()
