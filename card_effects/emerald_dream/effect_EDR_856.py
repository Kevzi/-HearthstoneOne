"""EDR_856 - Nightmare Lord Xavius"""
def on_battlecry(game, player, card, target=None):
    if not player.deck: return
    game.discover_card(player, player.deck, source_card=card)

def on_discover_selection(game, player, card, choice):
    # Draw selected minion and give Dark Gift
    player.draw_specific_card(choice)
    choice.add_buff("DARK_GIFT")
