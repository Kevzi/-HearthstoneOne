"""TIME_432 - Intertwined Fate: Discover a copy of a card from your deck and one from your opponent's."""

def on_play(game, player, card, target=None):
    import random
    
    # Get a random card from player's deck
    if player.deck:
        own_card = random.choice(player.deck)
        from simulator.factory import create_card
        copy = create_card(own_card.card_id, game)
        if copy:
            player.add_to_hand(copy)
    
    # Get a random card from opponent's deck (simplified - no discover UI)
    opponent = player.opponent
    if opponent and opponent.deck:
        opp_card = random.choice(opponent.deck)
        from simulator.factory import create_card
        copy = create_card(opp_card.card_id, game)
        if copy:
            player.add_to_hand(copy)
