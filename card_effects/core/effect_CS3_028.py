"""CS3_028 - Thrive in the Shadows"""
from simulator.enums import CardType

def on_play(game, player, card, target=None):
    # Discover a spell from your deck
    spells = [c for c in player.deck if c.card_type == CardType.SPELL]
    
    if not spells:
        return
        
    game.discover_card(player, spells, source_card=card)
    # Note: "Discover" usually draws the card in Hearthstone unless specified "copy".
    # Thrive in the Shadows says "Discover a spell from your deck". 
    # Usually implies drawing it. Rules check: It DRAWS it.
    
def on_discover_selection(game, player, card, choice):
    # Choice is the selected card instance from the discover pool
    if choice in player.deck:
        player.draw_specific_card(choice)
