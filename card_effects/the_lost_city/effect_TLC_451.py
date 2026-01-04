"""TLC_451 - Cursed Catacombs"""

def on_play(game, player, card, target=None):
    # Discover another card from your deck. Make it Temporary.
    if not player.deck:
        return
        
    game.discover_card(player, player.deck, source_card=card)

def on_discover_selection(game, player, card, choice):
    from simulator.factory import create_card
    # "Another card" usually means ID != this card ID? Or just distinct selection.
    # We take the copy.
    copy = create_card(choice.card_id, game)
    if copy:
        copy.is_temporary = True # Simulator flag for "Discard at end of turn"
        player.add_to_hand(copy)
