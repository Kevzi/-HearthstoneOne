"""EDR_891 - Ravenous Felhunter"""
from simulator.enums import CardType

def on_deathrattle(game, minion):
    owner = minion.controller
    
    # Resurrect a friendly Deathrattle minion that costs (4) or less.
    # We need a graveyard or 'dead_minions' list.
    
    candidates = []
    for m in owner.graveyard:
        if m.is_minion and m.cost <= 4 and m.has_deathrattle and m is not minion:
            candidates.append(m)
            
    if candidates:
        import random
        chosen = random.choice(candidates)
        
        # Summon a copy
        from simulator.factory import create_card
        # We need the ID
        copy = create_card(chosen.card_id, game)
        if copy:
            owner.summon(copy)
