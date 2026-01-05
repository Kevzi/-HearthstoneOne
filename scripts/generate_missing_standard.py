"""
Generate missing card effects for Standard format.

This script identifies all Standard cards without effects and generates them.
Run with: python scripts/generate_missing_standard.py
"""

import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from simulator import CardDatabase, CardData

# Standard 2026 Sets
STANDARD_SETS = [
    'CORE', 
    'WHIZBANGS_WORKSHOP', 
    'PERILS_IN_PARADISE', 
    'ISLAND_VACATION', 
    'THE_GREAT_DARK_BEYOND', 
    'SPACE', 
    'BATTLE_OF_THE_BANDS'
]

# Map set names to effect folder names
SET_TO_FOLDER = {
    'CORE': 'core',
    'WHIZBANGS_WORKSHOP': 'whizbangs_workshop', 
    'PERILS_IN_PARADISE': 'island_vacation',
    'ISLAND_VACATION': 'island_vacation',
    'THE_GREAT_DARK_BEYOND': 'great_dark_beyond',
    'SPACE': 'space',
    'BATTLE_OF_THE_BANDS': 'battle_of_the_bands'
}


def get_missing_cards():
    """Get all Standard cards that need effects but don't have them."""
    db = CardDatabase.get_instance()
    db.load()
    
    missing = []
    
    for card in db._cards.values():
        # Skip non-standard
        if card.card_set not in STANDARD_SETS:
            continue
            
        # Skip cards without meaningful text (vanilla minions)
        if not card.text or len(card.text.strip()) < 5:
            continue
            
        # Skip tokens and generated cards
        if 't' in card.card_id.lower() and card.card_id.count('_') > 1:
            continue
            
        # Check if effect exists
        folder = SET_TO_FOLDER.get(card.card_set, card.card_set.lower())
        effect_path = f'card_effects/{folder}/effect_{card.card_id}.py'
        
        if not os.path.exists(effect_path):
            missing.append(card)
    
    return missing


def generate_effect_code(card: CardData) -> str:
    """Generate Python effect code for a card based on its text."""
    text = card.text.lower()
    card_type = card.card_type.name if hasattr(card.card_type, 'name') else str(card.card_type)
    
    # Detect mechanics from text
    has_battlecry = 'battlecry' in text
    has_deathrattle = 'deathrattle' in text
    has_discover = 'discover' in text
    has_deal_damage = 'deal' in text and 'damage' in text
    has_draw = 'draw' in text
    has_summon = 'summon' in text
    has_destroy = 'destroy' in text
    has_give = 'give' in text
    has_gain = 'gain' in text
    has_restore = 'restore' in text or 'heal' in text
    has_taunt = 'taunt' in text and 'give' not in text
    has_rush = 'rush' in text and 'give' not in text
    has_divine_shield = 'divine shield' in text
    has_lifesteal = 'lifesteal' in text
    has_random = 'random' in text
    has_all = 'all ' in text
    has_friendly = 'friendly' in text
    has_enemy = 'enemy' in text or 'enemies' in text
    is_spell = card_type in ['SPELL', 'CardType.SPELL']
    
    # Extract numbers from text
    import re
    numbers = re.findall(r'\d+', card.text)
    amount = int(numbers[0]) if numbers else 1
    
    code_lines = [
        f'"""Effect for {card.name} ({card.card_id}).',
        f'',
        f'Card Text: {card.text}',
        f'"""',
        '',
    ]
    
    # Determine function type
    if is_spell:
        func_name = 'on_play'
        func_sig = 'def on_play(game, source, target):'
    elif has_battlecry:
        func_name = 'battlecry'
        func_sig = 'def battlecry(game, source, target):'
    elif has_deathrattle:
        func_name = 'deathrattle'
        func_sig = 'def deathrattle(game, source):'
    else:
        # Default to battlecry for minions with effects
        func_name = 'battlecry'
        func_sig = 'def battlecry(game, source, target):'
    
    code_lines.append(func_sig)
    code_lines.append('    player = source.controller')
    code_lines.append('    opponent = player.opponent')
    code_lines.append('')
    
    # Generate body based on mechanics
    body_lines = []
    
    if has_deal_damage:
        if has_all and has_enemy:
            body_lines.append(f'    # Deal {amount} damage to all enemies')
            body_lines.append(f'    for m in list(opponent.board):')
            body_lines.append(f'        game.deal_damage(m, {amount}, source)')
            body_lines.append(f'    game.deal_damage(opponent.hero, {amount}, source)')
        elif has_random:
            body_lines.append(f'    # Deal {amount} damage to a random enemy')
            body_lines.append(f'    import random')
            body_lines.append(f'    targets = list(opponent.board) + [opponent.hero]')
            body_lines.append(f'    if targets:')
            body_lines.append(f'        game.deal_damage(random.choice(targets), {amount}, source)')
        elif 'target' in func_sig:
            body_lines.append(f'    # Deal {amount} damage to target')
            body_lines.append(f'    if target:')
            body_lines.append(f'        game.deal_damage(target, {amount}, source)')
        else:
            body_lines.append(f'    # Deal {amount} damage')
            body_lines.append(f'    if opponent.hero:')
            body_lines.append(f'        game.deal_damage(opponent.hero, {amount}, source)')
    
    if has_draw:
        draw_count = amount if 'draw' in text else 1
        body_lines.append(f'    # Draw {draw_count} card(s)')
        body_lines.append(f'    player.draw({draw_count})')
    
    if has_summon:
        body_lines.append(f'    # Summon effect')
        body_lines.append(f'    # TODO: Implement summon logic for specific token')
        body_lines.append(f'    pass')
    
    if has_restore or 'heal' in text.lower():
        if has_all and has_friendly:
            body_lines.append(f'    # Restore {amount} Health to all friendly characters')
            body_lines.append(f'    for m in player.board:')
            body_lines.append(f'        game.heal(m, {amount}, source)')
            body_lines.append(f'    game.heal(player.hero, {amount}, source)')
        else:
            body_lines.append(f'    # Restore {amount} Health')
            body_lines.append(f'    if target:')
            body_lines.append(f'        game.heal(target, {amount}, source)')
    
    if has_give and (has_taunt or has_rush or has_divine_shield):
        body_lines.append(f'    # Give keywords')
        body_lines.append(f'    if target:')
        if 'taunt' in text:
            body_lines.append(f'        target._taunt = True')
        if 'rush' in text:
            body_lines.append(f'        target._rush = True')
        if 'divine shield' in text:
            body_lines.append(f'        target._divine_shield = True')
    
    if has_gain and 'armor' in text:
        body_lines.append(f'    # Gain {amount} Armor')
        body_lines.append(f'    player.hero.gain_armor({amount})')
    
    if has_destroy:
        if has_random:
            body_lines.append(f'    # Destroy a random enemy minion')
            body_lines.append(f'    import random')
            body_lines.append(f'    if opponent.board:')
            body_lines.append(f'        target = random.choice(opponent.board)')
            body_lines.append(f'        target.destroy()')
        elif 'target' in func_sig:
            body_lines.append(f'    # Destroy target')
            body_lines.append(f'    if target:')
            body_lines.append(f'        target.destroy()')
    
    if has_discover:
        body_lines.append(f'    # Discover effect')
        body_lines.append(f'    # TODO: Implement discover with proper card pool')
        body_lines.append(f'    pass')
    
    # If no specific mechanics detected, add a pass
    if not body_lines:
        body_lines.append(f'    # Effect: {card.text}')
        body_lines.append(f'    # TODO: Implement')
        body_lines.append(f'    pass')
    
    code_lines.extend(body_lines)
    
    return '\n'.join(code_lines)


def save_effect(card: CardData, code: str):
    """Save the generated effect code to the appropriate file."""
    folder = SET_TO_FOLDER.get(card.card_set, card.card_set.lower())
    dir_path = f'card_effects/{folder}'
    
    # Create directory if needed
    os.makedirs(dir_path, exist_ok=True)
    
    file_path = f'{dir_path}/effect_{card.card_id}.py'
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(code)
    
    return file_path


def main():
    print("=== Standard Card Effect Generator ===\n")
    
    missing = get_missing_cards()
    print(f"Found {len(missing)} cards without effects.\n")
    
    if not missing:
        print("All Standard cards have effects!")
        return
    
    # Group by set for reporting
    by_set = {}
    for card in missing:
        by_set.setdefault(card.card_set, []).append(card)
    
    print("Missing by set:")
    for s, cards in sorted(by_set.items()):
        print(f"  {s}: {len(cards)}")
    
    print(f"\nGenerating effects...")
    
    generated = 0
    errors = 0
    
    for i, card in enumerate(missing):
        try:
            code = generate_effect_code(card)
            path = save_effect(card, code)
            generated += 1
            
            if (i + 1) % 50 == 0:
                print(f"  Progress: {i+1}/{len(missing)} ({generated} generated)")
                
        except Exception as e:
            errors += 1
            print(f"  Error for {card.card_id}: {e}")
    
    print(f"\n=== Complete ===")
    print(f"Generated: {generated}")
    print(f"Errors: {errors}")


if __name__ == "__main__":
    main()
