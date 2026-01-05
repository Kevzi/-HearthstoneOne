"""Effect for Prize Vendor (CORE_DMF_067).

Card Text: <b>Battlecry and Deathrattle:</b> Each player draws a card.
"""

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Draw 1 card(s)
    player.draw(1)