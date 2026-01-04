"""TIME_039 - Deja Vu"""

def on_play(game, player, card, target=None):
    # Discover a copy of a card in your opponent's hand. It costs (1) less.
    opponent = player.opponent
    if not opponent.hand:
        return
        
    game.discover_card(player, opponent.hand, source_card=card)

def on_discover_selection(game, player, card, choice):
    # Choice is reference to opponent card. We need a Copy.
    from simulator.factory import create_card
    copy = create_card(choice.card_id, game)
    if copy:
        copy.cost = max(0, copy.cost - 1)
        player.add_to_hand(copy)
