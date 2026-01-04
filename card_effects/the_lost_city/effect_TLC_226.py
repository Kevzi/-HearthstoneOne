"""TLC_226 - Conjured Bookkeeper"""
from simulator.enums import CardType

def on_deathrattle(game, minion):
    owner = minion.controller
    # Draw a spell.
    spells = [c for c in owner.deck if c.card_type == CardType.SPELL]
    if spells:
        import random
        owner.draw_specific_card(random.choice(spells))
    
    # Kindred: Summon a copy of this.
    # Kindred usually means "If you controlled another minion of same type/race"
    # But for TLC (The Lost City), it often means "If you control a specific type". 
    # Card is likely an Elemental or similar.
    if owner.has_kindred_active: # Simulator flag
        from simulator.factory import create_card
        copy = create_card("TLC_226", game)
        owner.summon(copy)
