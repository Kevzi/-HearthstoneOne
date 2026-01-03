"""CORE_AV_329 - Thrive in the Shadows: Discover a Shadow spell from your deck."""

def on_play(game, player, card, target=None):
    import random
    
    # Find Shadow spells in deck
    shadow_spells = [c for c in player.deck 
                     if hasattr(c, 'data') and c.data 
                     and c.data.card_type.name == 'SPELL'
                     and 'shadow' in c.data.text.lower() if c.data.text else False]
    
    # Fallback: any spell from deck
    if not shadow_spells:
        shadow_spells = [c for c in player.deck 
                        if hasattr(c, 'data') and c.data 
                        and c.data.card_type.name == 'SPELL']
    
    if shadow_spells:
        chosen = random.choice(shadow_spells)
        # Move from deck to hand
        if chosen in player.deck:
            player.deck.remove(chosen)
            player.add_to_hand(chosen)
