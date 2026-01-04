import json
import os
import re

ARENA_POOL = "data/arena_pool.json"
EFFECTS_DIR = "card_effects"

# Keywords mapped to their implementation logic
KEYWORDS = {
    "Taunt": "minion.taunt = True",
    "Divine Shield": "minion.divine_shield = True",
    "Rush": "minion.rush = True",
    "Charge": "minion.charge = True",
    "Stealth": "minion.stealth = True",
    "Windfury": "minion.windfury = True",
    "Reborn": "minion.reborn = True",
    "Lifesteal": "minion.lifesteal = True",
    "Poisonous": "minion.poisonous = True",
    "Elusive": "minion.elusive = True", # Often called "Can't be targeted by spells or Hero Powers"
}

# Regex to detect vanilla text or simple keyword soup
# We want to avoid Battlecries, Deathrattles, active effects, etc.
COMPLEX_PATTERNS = [
    r"Battlecry", r"Deathrattle", r"Combo", r"Outcast", r"Finale", 
    r"Discover", r"If you", r"Whenever", r"After", r"Start of", r"End of",
    r"Cost", r"Draw", r"Deal", r"Restore", r"Gain", r"Summon", r"Add",
    r"Choose One", r"Titan", r"Colossal", r"Excavate", r"Tradeable", r"Forge"
]

def sanitize_set_name(name):
    return name.lower()

def impl_exists(card_id, set_name):
    path = os.path.join(EFFECTS_DIR, sanitize_set_name(set_name), f"effect_{card_id}.py")
    return os.path.exists(path)

def normalize_text(text):
    if not text: return ""
    # Remove HTML tags
    clean = re.sub(r'<[^>]+>', '', text)
    # Remove [x]
    clean = clean.replace("[x]", "")
    return clean.strip()

def is_simple_card(card):
    # Minions only for now
    if card.get('type') != 'MINION':
        return False, []
        
    text = normalize_text(card.get('text', ''))
    
    # If empty text -> Vanilla -> YES
    if not text:
        return True, []
        
    # Check for complex triggers
    for pattern in COMPLEX_PATTERNS:
        if re.search(pattern, text, re.IGNORECASE):
            return False, []
            
    # Check if text is ONLY keywords (comma or newline separated)
    # Example: "Taunt, Divine Shield"
    # We strip known keywords and see if anything remains
    remaining = text
    found_ops = []
    
    for kw, op in KEYWORDS.items():
        if re.search(r'\b' + re.escape(kw) + r'\b', remaining, re.IGNORECASE):
            found_ops.append(op)
            remaining = re.sub(r'\b' + re.escape(kw) + r'\b', '', remaining, flags=re.IGNORECASE)
            
    # Cleanup punctuation
    remaining = re.sub(r'[,.\n\r]', '', remaining).strip()
    
    if not remaining:
        return True, found_ops
        
    return False, []

def generate_code(card, ops):
    card_id = card['id']
    name = card.get('name', 'Unknown')
    text = normalize_text(card.get('text', ''))
    
    code = f'"""\n{name} ({card_id})\n{text}\n"""\n'
    code += "# Vanilla or Keyword-only minion. \n"
    code += "# Logic is handled by the simulator engine based on JSON stats and mechanics.\n"
    
    return code

def main():
    print("Bulk importing simple Arena cards...")
    
    with open(ARENA_POOL, 'r', encoding='utf-8') as f:
        pool = json.load(f)
        
    count = 0
    sets_processed = set()
    
    for card in pool:
        card_id = card['id']
        set_name = card.get('set', 'CORE')
        
        # Skip if already implemented
        if impl_exists(card_id, set_name):
            continue
            
        simple, ops = is_simple_card(card)
        
        if simple:
            # Create directory
            dir_path = os.path.join(EFFECTS_DIR, sanitize_set_name(set_name))
            os.makedirs(dir_path, exist_ok=True)
            
            # Write file
            file_path = os.path.join(dir_path, f"effect_{card_id}.py")
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(generate_code(card, ops))
                
            count += 1
            sets_processed.add(set_name)
            
    print(f"Generated {count} new simple card effects.")
    print(f"Impacted sets: {', '.join(sorted(sets_processed))}")

if __name__ == "__main__":
    main()
