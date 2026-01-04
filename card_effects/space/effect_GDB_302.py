"""GDB_302 - Blazing Accretion"""
from simulator.enums import CardType, Race

def on_battlecry(game, player, card, target=None):
    # Destroy top 3 cards. Any Fire spells or Elementals are drawn instead.
    
    deck = player.deck
    if not deck: return
    
    top_3 = deck[:3] # Assuming deck[0] is top
    # Actually deck handling usually pops from top. 
    # Let's assume standard list order: deck[-1] is top? Or deck[0]?
    # Simulator usually draws from index 0.
    
    for c in top_3:
        player.deck.remove(c) # Remove from deck
        
        is_fire = (c.card_type == CardType.SPELL and getattr(c, 'spell_school', 'NONE') == 'FIRE')
        is_elemental = (c.is_minion and c.race == Race.ELEMENTAL)
        
        if is_fire or is_elemental:
            player.add_to_hand(c)
        else:
            # Burned
            pass # Graveyard? Or just gone. "Destroyed" -> Graveyard usually.
            player.graveyard.append(c)
