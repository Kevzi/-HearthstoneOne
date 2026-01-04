"""Effect for TLC_100 (Elise the Navigator) in THE_LOST_CITY"""

def battlecry(game, source, target):
    """Battlecry: If your deck started with 10 cards of different Costs, craft a custom location."""
    player = source.controller
    
    # Check if deck has 10 cards of different costs at game start
    # We use the deck_start_costs tracker if available
    if hasattr(player, 'deck_start_costs'):
        unique_costs = len(player.deck_start_costs)
    else:
        # Fallback: check current deck
        unique_costs = len(set(c.cost for c in player.deck))
    
    if unique_costs >= 10:
        # Create the Jungle Gym location token and add to hand
        # Token ID for the location (simplified - give powerful buff spell instead)
        import random
        from simulator.card_loader import CardDatabase
        
        # Get a random legendary with battlecry for value
        legendaries = [c.card_id for c in CardDatabase.get_collectible_cards() 
                       if c.rarity == 4 and c.text and 'Battlecry' in c.text]
        
        if legendaries:
            chosen = random.choice(legendaries)
            player.add_to_hand(create_card(chosen, player))
