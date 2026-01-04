"""EDR_572 - Tormented Dreadwing"""
from simulator.enums import Race

def on_deathrattle(game, minion):
    owner = minion.controller
    # Draw 2 Dragons. Reduce their Costs by (1).
    
    dragons_in_deck = [c for c in owner.deck if c.is_minion and c.race == Race.DRAGON]
    if not dragons_in_deck:
        return
        
    import random
    # Draw up to 2
    to_draw = random.sample(dragons_in_deck, min(2, len(dragons_in_deck)))
    
    for c in to_draw:
        owner.draw_specific_card(c)
        c.cost = max(0, c.cost - 1)
