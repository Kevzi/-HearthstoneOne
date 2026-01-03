"""TLC_100 - Elise the Navigator: Battlecry: If your deck started with 10 cards of different Costs, craft a custom location."""

def on_play(game, player, card, target=None):
    # Check if deck has 10 cards of different costs
    # Simplified: just check current deck
    costs = set()
    for c in player.deck:
        costs.add(c.cost)
    
    if len(costs) >= 10:
        # Create a location (simplified - create a generic good card)
        from simulator.factory import create_card
        # Location placeholder - would need actual location implementation
        pass
