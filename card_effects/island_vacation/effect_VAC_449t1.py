"""Effect for Carress, Cabaret Star (VAC_449t1).

Card Text: <b>Battlecry:</b> Draw 2 cards.
<b>Freeze</b> three random enemy minions.
"""

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    # Draw 2 card(s)
    player.draw(2)